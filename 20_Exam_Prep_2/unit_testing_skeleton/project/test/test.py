from unittest import TestCase, main
from project.railway_station import RailwayStation
from collections import deque


class TestRailwayStation(TestCase):

    def setUp(self):
        self.railway_station = RailwayStation("plovdiv")

    def test_correct_init(self):
        self.assertEqual("plovdiv", self.railway_station.name)

    def test_init_with_invalid_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.railway_station.name = "asd"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board_success(self):
        self.railway_station.new_arrival_on_board("za burgas")

        self.assertEqual(deque(["za burgas"]), self.railway_station.arrival_trains)

    def test_train_has_arrived_when_there_is_another_trains_before_current_train_info(self):
        self.railway_station.arrival_trains.append("za varna")
        self.railway_station.arrival_trains.append("za sofiq")
        expected_message = f"There are other trains to arrive before za burgas."

        result = self.railway_station.train_has_arrived("za burgas")

        self.assertEqual(expected_message, result)

    def test_train_has_arrived_success(self):
        self.railway_station.arrival_trains.append("za varna")
        expected_message = "za varna is on the platform and will leave in 5 minutes."
        result = self.railway_station.train_has_arrived("za varna")
        self.assertEqual(expected_message, result)

    def test_train_has_left_when_train_is_on_first_position_expected_true(self):
        self.railway_station.departure_trains.append("za plovdiv")

        result = self.railway_station.train_has_left("za plovdiv")

        self.assertTrue(result)

    def test_railway_station_when_there_is_other_trains_before_current_train_expected_false(self):
        self.railway_station.departure_trains.append("za plovdiv")
        self.railway_station.departure_trains.append("za varna")
        self.railway_station.departure_trains.append("za burgas")

        result = self.railway_station.train_has_left("za varna")

        self.assertFalse(result)


if __name__ == '__main__':
    main()
