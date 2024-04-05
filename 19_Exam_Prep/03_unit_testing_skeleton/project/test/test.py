from unittest import TestCase, main
from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):

    def setUp(self) -> None:
        self.robot = ClimbingRobot("Alpine", "ram", 100, 200)

        self.robot_with_installed_software = ClimbingRobot("Alpine", "ram", 100, 200)

        self.robot_with_installed_software.installed_software = [
            {"name": "PyCharm", "capacity_consumption": 50, "memory_consumption": 49},
            {"name": "CLion", "capacity_consumption": 49, "memory_consumption": 51}]

    def test_correct_init(self):
        self.assertEqual("Alpine", self.robot.category)
        self.assertEqual("ram", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(200, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_create_robot_with_invalid_category(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "invalid"

        self.assertEqual(f"Category should be one of {self.robot.ALLOWED_CATEGORIES}", str(ve.exception))

    def test_get_used_capacity_expected_success(self):
        result = self.robot_with_installed_software.get_used_capacity()

        self.assertEqual(99, result)

    def test_get_available_capacity_expected_success(self):
        expected_result = self.robot_with_installed_software.capacity - \
                          sum(s['capacity_consumption'] for s in self.robot_with_installed_software.installed_software)
        result = self.robot_with_installed_software.get_available_capacity()

        self.assertEqual(result, expected_result)

    def test_get_used_memory_expected_success(self):
        result = self.robot_with_installed_software.get_used_memory()

        self.assertEqual(100, result)

    def test_get_available_memory_expected_success(self):
        expected_result = self.robot_with_installed_software.memory - \
                          sum(s['memory_consumption'] for s in self.robot_with_installed_software.installed_software)
        result = self.robot_with_installed_software.get_available_memory()

        self.assertEqual(result, expected_result)

    def test_install_software_with_max_equal_values_expect_success(self):
        result = self.robot.install_software(
            {"name": "PyCharm", "capacity_consumption": 100, "memory_consumption": 200})

        self.assertEqual(f"Software 'PyCharm' successfully installed on Alpine part.",
                         result)

        self.assertEqual(self.robot.installed_software,
                         [{"name": "PyCharm", "capacity_consumption": 100, "memory_consumption": 200}])

    def test_install_software_with_less_than_max_values_expect_success(self):
        result = self.robot.install_software(
            {"name": "PyCharm", "capacity_consumption": 10, "memory_consumption": 20}, )

        self.assertEqual(
            f"Software 'PyCharm' successfully installed on Alpine part.",
            result)

        self.assertEqual(
            self.robot.installed_software,
            [{"name": "PyCharm", "capacity_consumption": 10, "memory_consumption": 20}])

    def test_install_software_with_one_value_greater_than_max_values_return_error_message(self):
        result = self.robot.install_software(
            {"name": "PyCharm", "capacity_consumption": 10, "memory_consumption": 2000}, )

        self.assertEqual(f"Software 'PyCharm' cannot be installed on Alpine part.", result)
        self.assertEqual(self.robot.installed_software, [])

    def test_install_software_with_both_value_greater_than_max_values_return_error_message(self):
        result = self.robot_with_installed_software.install_software(
            {"name": "PyCharm", "capacity_consumption": 49, "memory_consumption": 50}, )

        self.assertEqual(f"Software 'PyCharm' cannot be installed on Alpine part.", result)
        self.assertEqual(self.robot.installed_software, [])


if __name__ == '__main__':
    main()
