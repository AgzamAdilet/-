class RoomBookingSystem:
    def book_room(self, name):
        print(f"Номер забронирован для {name}")

    def cancel_booking(self, name):
        print(f"Бронь для {name} отменена")


class RestaurantSystem:
    def reserve_table(self, name):
        print(f"Стол забронирован для {name}")

    def order_food(self, food):
        print(f"Заказано блюдо: {food}")


class EventManagementSystem:
    def organize_event(self, event_name):
        print(f"Организовано мероприятие: {event_name}")

    def book_equipment(self):
        print("Оборудование забронировано")


class CleaningService:
    def schedule_cleaning(self, room):
        print(f"Уборка запланирована для комнаты {room}")

    def clean_now(self, room):
        print(f"Комната {room} убрана")


class TaxiService:
    def call_taxi(self):
        print("Такси вызвано")

class HotelFacade:
    def __init__(self):
        self.room = RoomBookingSystem()
        self.restaurant = RestaurantSystem()
        self.event = EventManagementSystem()
        self.cleaning = CleaningService()
        self.taxi = TaxiService()

    def book_room_with_services(self, name):
        print("\n--- Бронирование номера с услугами ---")
        self.room.book_room(name)
        self.restaurant.order_food("Ужин")
        self.cleaning.schedule_cleaning(101)

    def organize_event_full(self, event_name, guests):
        print("\n--- Организация мероприятия ---")
        self.event.organize_event(event_name)
        self.event.book_equipment()
        for guest in guests:
            self.room.book_room(guest)

    def reserve_table_with_taxi(self, name):
        print("\n--- Ресторан + такси ---")
        self.restaurant.reserve_table(name)
        self.taxi.call_taxi()

    def cancel_room(self, name):
        self.room.cancel_booking(name)

    def request_cleaning(self, room):
        self.cleaning.clean_now(room)

if __name__ == "__main__":
    hotel = HotelFacade()

    hotel.book_room_with_services("Ali")
    hotel.organize_event_full("Conference", ["Ali", "Dana"])
    hotel.reserve_table_with_taxi("Bek")

    hotel.request_cleaning(101)
    hotel.cancel_room("Ali")
