from unittest import TestCase, main
# from car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("benz", "e200", 10, 60)

    def test_correct_init(self):
        self.assertEqual("benz", self.car.make)
        self.assertEqual("e200", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_with_empty_string_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_with_empty_string_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_with_zero_or_negative_value_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_zero_or_negative_value_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_with_negative_value_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -10

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_zero_or_negative_amount_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_correct_increase_fuel_amount(self):
        result = self.car.fuel_amount + 60
        self.car.refuel(80)
        self.assertEqual(result, self.car.fuel_amount)

    def test_drive_without_needed_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_correct_fuel_amount_decrease_expect(self):
        self.car.fuel_amount = 60
        self.car.drive(100)

        self.assertEqual(50, self.car.fuel_amount)


if __name__ == '__main__':
    main()
