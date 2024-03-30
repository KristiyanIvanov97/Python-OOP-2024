from unittest import TestCase, main
# from extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self) -> None:
        self.integer_list = IntegerList(1, 2, 3, "hello", 2.5)

    def test_correct_init(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_when_element_is_not_integer_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add("hello")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_element_correct_append_element_to_data(self):
        expected_result = [1, 2, 3, 8]

        self.integer_list.add(8)
        self.assertEqual(expected_result, self.integer_list.get_data())

    def test_remove_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(10)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_valid_index_del_correct_value_of_index(self):
        index = 2
        value = self.integer_list.get_data()[index]

        result = self.integer_list.remove_index(index)
        self.assertEqual(value, result)

    def test_get_value_by_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(10)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_value_by_valid_index_return_correct_value(self):
        index = 2
        value = self.integer_list.get_data()[index]

        result = self.integer_list.get(index)
        self.assertEqual(value, result)

    def test_insert_element_by_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(10, 8)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_non_integer_element_by_valid_index_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(1, "kkk")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_correct_element_by_valid_index(self):
        self.integer_list.insert(0, 100)
        self.assertEqual([100, 1, 2, 3], self.integer_list.get_data())

    def test_get_biggest_element_correct(self):
        self.assertEqual(3, self.integer_list.get_biggest())

    def test_get_index_correct(self):
        self.assertEqual(1, self.integer_list.get_index(2))


if __name__ == '__main__':
    main()
