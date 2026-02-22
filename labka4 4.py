import threading
import json
import copy
from abc import ABC, abstractmethod

class ConfigurationManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._settings = {}
        return cls._instance

    def set(self, key, value):
        self._settings[key] = value

    def get(self, key):
        if key not in self._settings:
            raise KeyError(f"Setting '{key}' not found!")
        return self._settings[key]

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump(self._settings, f)

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                self._settings = json.load(f)
        except FileNotFoundError:
            print("Config file not found!")

class Report:
    def __init__(self):
        self.header = ""
        self.content = ""
        self.footer = ""

    def __str__(self):
        return f"{self.header}\n{self.content}\n{self.footer}"


class IReportBuilder(ABC):
    @abstractmethod
    def set_header(self, header): pass

    @abstractmethod
    def set_content(self, content): pass

    @abstractmethod
    def set_footer(self, footer): pass

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

    def get_report(self):
        return self.report


class ReportDirector:
    def construct(self, builder: IReportBuilder):
        builder.set_header("Report Title")
        builder.set_content("This is report content")
        builder.set_footer("2026")
        return builder.get_report()

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def clone(self):
        return copy.deepcopy(self)


class Discount:
    def __init__(self, percent):
        self.percent = percent

    def clone(self):
        return copy.deepcopy(self)


class Order:
    def __init__(self, products, delivery_cost, discount, payment_method):
        self.products = products
        self.delivery_cost = delivery_cost
        self.discount = discount
        self.payment_method = payment_method

    def clone(self):
        return copy.deepcopy(self)

    def total_price(self):
        total = sum(p.price * p.quantity for p in self.products)
        total += self.delivery_cost
        if self.discount:
            total *= (1 - self.discount.percent / 100)
        return total

if __name__ == "__main__":

    print("===== SINGLETON TEST =====")

    def worker():
        config = ConfigurationManager()
        print("Instance ID:", id(config))

    threads = []
    for _ in range(3):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    config = ConfigurationManager()
    config.set("theme", "dark")
    config.save_to_file("config.json")

    print("\n===== BUILDER TEST =====")

    director = ReportDirector()

    text_report = director.construct(TextReportBuilder())
    html_report = director.construct(HtmlReportBuilder())

    print("\nTEXT REPORT:")
    print(text_report)

    print("\nHTML REPORT:")
    print(html_report)

    print("\n===== PROTOTYPE TEST =====")

    p1 = Product("Laptop", 1000, 1)
    discount = Discount(10)

    order1 = Order([p1], 50, discount, "Card")
    order2 = order1.clone()

    order2.products[0].quantity = 2

    print("Order1 total:", order1.total_price())
    print("Order2 total:", order2.total_price())