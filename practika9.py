class TV:
    def on(self):
        print("TV включен")

    def off(self):
        print("TV выключен")

    def set_channel(self, channel):
        print(f"TV переключен на канал {channel}")


class AudioSystem:
    def on(self):
        print("Аудиосистема включена")

    def off(self):
        print("Аудиосистема выключена")

    def set_volume(self, volume):
        print(f"Громкость установлена на {volume}")


class DVDPlayer:
    def play(self):
        print("DVD воспроизводится")

    def pause(self):
        print("DVD на паузе")

    def stop(self):
        print("DVD остановлен")


class GameConsole:
    def on(self):
        print("Игровая консоль включена")

    def start_game(self):
        print("Игра запущена")


class HomeTheaterFacade:
    def __init__(self, tv, audio, dvd, console):
        self.tv = tv
        self.audio = audio
        self.dvd = dvd
        self.console = console

    def watch_movie(self):
        print("\n--- Просмотр фильма ---")
        self.tv.on()
        self.tv.set_channel("HDMI")
        self.audio.on()
        self.audio.set_volume(10)
        self.dvd.play()

    def end_movie(self):
        print("\n--- Выключение системы ---")
        self.dvd.stop()
        self.audio.off()
        self.tv.off()

    def play_game(self):
        print("\n--- Запуск игры ---")
        self.tv.on()
        self.audio.on()
        self.console.on()
        self.console.start_game()

    def listen_music(self):
        print("\n--- Прослушивание музыки ---")
        self.tv.on()
        self.audio.on()
        self.audio.set_volume(7)

    def set_volume(self, volume):
        self.audio.set_volume(volume)



if __name__ == "__main__":
    tv = TV()
    audio = AudioSystem()
    dvd = DVDPlayer()
    console = GameConsole()

    home_theater = HomeTheaterFacade(tv, audio, dvd, console)

    home_theater.watch_movie()
    home_theater.set_volume(15)
    home_theater.end_movie()

    home_theater.play_game()
    home_theater.listen_music()
