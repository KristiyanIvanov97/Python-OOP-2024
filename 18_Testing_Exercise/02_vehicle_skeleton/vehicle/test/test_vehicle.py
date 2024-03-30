from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(50, 100)

    def test_correct_init(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_default_fuel_consumption(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_without_needed_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_expect_fuel_decrease(self):
        self.vehicle.drive(10)

        self.assertEqual(37.5, self.vehicle.fuel)

    def test_refuel_too_much_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_expected_fuel_increase(self):
        self.vehicle.fuel = 20

        self.vehicle.refuel(20)
        self.assertEqual(40, self.vehicle.fuel)

    def test_correct_string_repr_of_vehicle(self):
        result = "The vehicle has 100 " \
                 f"horse power with 50 fuel left and 1.25 fuel consumption"

        self.assertEqual(result, str(self.vehicle))


if __name__ == '__main__':
    main()
