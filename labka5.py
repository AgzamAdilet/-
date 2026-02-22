import threading
import json
import os
import time
import copy
from abc import ABC, abstractmethod
from datetime import datetime

class LogLevel:
    INFO = 1
    WARNING = 2
    ERROR = 3


class Logger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, config_file="logger_config.json"):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._init(config_file)
        return cls._instance

    def _init(self, config_file):
        self.config_file = config_file
        self.log_level = LogLevel.INFO
        self.log_file = "app.log"
        self.max_size = 5000
        self._file_lock = threading.Lock()
        self._load_config()

    def _load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as f:
                data = json.load(f)
                self.log_level = data.get("log_level", 1)
                self.log_file = data.get("log_file", "app.log")

    def set_log_level(self, level):
        self.log_level = level

    def _rotate_log(self):
        if os.path.exists(self.log_file):
            if os.path.getsize(self.log_file) >= self.max_size:
                os.rename(self.log_file, f"app_{int(time.time())}.log")

    def log(self, message, level):
        if level < self.log_level:
            return

        with self._file_lock:
            self._rotate_log()
            with open(self.log_file, "a") as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                level_name = {1: "INFO", 2: "WARNING", 3: "ERROR"}[level]
                f.write(f"[{timestamp}] [{level_name}] {message}\n")
                print(f"[{level_name}] {message}")  # console output


class LogReader:
    def __init__(self, file):
        self.file = file

    def read(self, min_level=LogLevel.INFO):
        if not os.path.exists(self.file):
            print("Log file not found")
            return

        with open(self.file, "r") as f:
            for line in f:
                if ("INFO" in line and min_level <= 1) or \
                   ("WARNING" in line and min_level <= 2) or \
                   ("ERROR" in line and min_level <= 3):
                    print(line.strip())

class ReportStyle:
    def __init__(self, bg_color="white", font_color="black", font_size=12):
        self.bg_color = bg_color
        self.font_color = font_color
        self.font_size = font_size


class Report:
    def __init__(self):
        self.header = ""
        self.content = ""
        self.footer = ""
        self.sections = []
        self.style = None

    def export(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(self))

    def __str__(self):
        result = f"{self.header}\n"
        for name, content in self.sections:
            result += f"\n{name}\n{content}\n"
        result += f"\n{self.footer}"
        return result


class IReportBuilder(ABC):

    @abstractmethod
    def set_header(self, header): pass

    @abstractmethod
    def set_content(self, content): pass

    @abstractmethod
    def set_footer(self, footer): pass

    @abstractmethod
    def add_section(self, name, content): pass

    @abstractmethod
    def set_style(self, style): pass

    @abstractmethod
    def get_report(self): pass


class TextReportBuilder(IReportBuilder):
    def __init__(self):
        self.report = Report()

    def set_header(self, header):
        self.report.header = f"*** {header} ***"

    def set_content(self, content):
        self.report.content = content

    def set_footer(self, footer):
        self.report.footer = f"--- {footer} ---"

    def add_section(self, name, content):
        self.report.sections.append((name, content))

    def set_style(self, style):
        self.report.style = style

    def get_report(self):
        return self.report


class HtmlReportBuilder(IReportBuilder):
    def __init__(self):
        self.report = Report()

    def set_header(self, header):
        self.report.header = f"<h1>{header}</h1>"

    def set_content(self, content):
        self.report.content = f"<p>{content}</p>"

    def set_footer(self, footer):
        self.report.footer = f"<footer>{footer}</footer>"

    def add_section(self, name, content):
        self.report.sections.append((f"<h2>{name}</h2>", f"<p>{content}</p>"))

    def set_style(self, style):
        self.report.style = style

    def get_report(self):
        return self.report


class ReportDirector:
    def construct(self, builder, style):
        builder.set_header("Game Report")
        builder.add_section("Statistics", "Player stats here")
        builder.add_section("Achievements", "Unlocked achievements")
        builder.set_footer("2026 ©")
        builder.set_style(style)
        return builder.get_report()

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def clone(self):
        return copy.deepcopy(self)


class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def clone(self):
        return copy.deepcopy(self)


class Skill:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def clone(self):
        return copy.deepcopy(self)


class Character:
    def __init__(self, health, strength, agility, intelligence, weapon, armor, skills):
        self.health = health
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.weapon = weapon
        self.armor = armor
        self.skills = skills

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"HP:{self.health}, STR:{self.strength}, Weapon:{self.weapon.name}"

if __name__ == "__main__":

    print("\n===== LOGGER TEST =====")

    logger = Logger()
    logger.set_log_level(LogLevel.INFO)

    def worker(name):
        logger.log(f"{name} started", LogLevel.INFO)
        logger.log(f"{name} warning!", LogLevel.WARNING)
        logger.log(f"{name} error!", LogLevel.ERROR)

    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(f"Thread-{i}",))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n===== REPORT BUILDER TEST =====")

    style = ReportStyle("gray", "blue", 14)
    director = ReportDirector()

    text_report = director.construct(TextReportBuilder(), style)
    html_report = director.construct(HtmlReportBuilder(), style)

    text_report.export("report.txt")
    html_report.export("report.html")

    print(text_report)

    print("\n===== PROTOTYPE TEST =====")

    sword = Weapon("Sword", 50)
    armor = Armor("Steel Armor", 30)
    skill1 = Skill("Fireball", 100)

    hero = Character(100, 20, 15, 10, sword, armor, [skill1])
    clone_hero = hero.clone()
    clone_hero.health = 200

    print("Original:", hero)
    print("Clone:", clone_hero)
