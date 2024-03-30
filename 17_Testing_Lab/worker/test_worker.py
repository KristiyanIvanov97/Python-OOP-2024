from unittest import TestCase, main

# from worker import Worker


class TestWorker(TestCase):

    def setUp(self):
        self.worker = Worker("ivan", 3000, 100)

    def test_correct_init(self):
        self.assertEqual("ivan", self.worker.name)
        self.assertEqual(3000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_with_no_energy_raises_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_with_energy_expected_money_increase_and_energy_decrease(self):
        expected_money = self.worker.money + self.worker.salary
        expected_energy = self.worker.energy - 1

        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_rest_expected_energy_increase_by_one(self):
        expected_energy = self.worker.energy + 1
        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_correct(self):
        expected_message = "ivan has saved 0 money."

        self.assertEqual(expected_message, self.worker.get_info())


if __name__ == '__main__':
    main()
