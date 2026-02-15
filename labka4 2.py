from abc import ABC, abstractmethod

class IVehicle(ABC):

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass

class Car(IVehicle):
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def drive(self):
        print(f"Car {self.brand} {self.model} is driving.")

    def refuel(self):
        print(f"Car refueled with {self.fuel_type}.")


class Motorcycle(IVehicle):
    def __init__(self, moto_type, engine_volume):
        self.moto_type = moto_type
        self.engine_volume = engine_volume

    def drive(self):
        print(f"{self.moto_type} motorcycle with {self.engine_volume}cc is driving.")

    def refuel(self):
        print("Motorcycle refueled.")


class Truck(IVehicle):
    def __init__(self, capacity, axles):
        self.capacity = capacity
        self.axles = axles

    def drive(self):
        print(f"Truck with {self.capacity} tons capacity is driving.")

    def refuel(self):
        print("Truck refueled.")

class Bus(IVehicle):
    def __init__(self, seats):
        self.seats = seats

    def drive(self):
        print(f"Bus with {self.seats} seats is driving.")

    def refuel(self):
        print("Bus refueled.")

class VehicleFactory(ABC):

    @abstractmethod
    def create_vehicle(self):
        pass

class CarFactory(VehicleFactory):
    def create_vehicle(self):
        brand = input("Enter car brand: ")
        model = input("Enter car model: ")
        fuel = input("Enter fuel type: ")
        return Car(brand, model, fuel)


class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self):
        moto_type = input("Enter motorcycle type: ")
        engine = input("Enter engine volume (cc): ")
        return Motorcycle(moto_type, engine)


class TruckFactory(VehicleFactory):
    def create_vehicle(self):
        capacity = input("Enter truck capacity (tons): ")
        axles = input("Enter number of axles: ")
        return Truck(capacity, axles)


class BusFactory(VehicleFactory):
    def create_vehicle(self):
        seats = input("Enter number of seats: ")
        return Bus(seats)

def main():
    print("Choose vehicle type:")
    print("1 - Car")
    print("2 - Motorcycle")
    print("3 - Truck")
    print("4 - Bus")

    choice = input("Your choice: ")

    if choice == "1":
        factory = CarFactory()
    elif choice == "2":
        factory = MotorcycleFactory()
    elif choice == "3":
        factory = TruckFactory()
    elif choice == "4":
        factory = BusFactory()
    else:
        print("Invalid choice!")
        return

    vehicle = factory.create_vehicle()
    vehicle.drive()
    vehicle.refuel()


if __name__ == "__main__":
    main()


