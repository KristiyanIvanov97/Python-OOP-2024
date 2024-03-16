from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: int) -> None:
        pass


class Car(Vehicle, ABC):
    CONDITIONER_ON = 0.90

    def drive(self, distance: int) -> None:
        consumption = (self.fuel_consumption + self.CONDITIONER_ON) * distance
        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle, ABC):
    CONDITIONER_ON = 1.6
    TOTAL_REFUEL = 0.95

    def drive(self, distance: int) -> None:
        consumption = (self.fuel_consumption + self.CONDITIONER_ON) * distance
        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel * self.TOTAL_REFUEL


