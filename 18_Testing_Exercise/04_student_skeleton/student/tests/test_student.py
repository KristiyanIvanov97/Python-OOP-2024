from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self) -> None:
        self.student_without_courses = Student("test")
        self.student = Student("Kris", {"basic": ["note1", "note2"]})

    def test_correct_init(self):
        self.assertEqual("Kris", self.student.name)
        self.assertEqual("test", self.student_without_courses.name)

        self.assertEqual({}, self.student_without_courses.courses)
        self.assertEqual({"basic": ["note1", "note2"]}, self.student.courses)

    def test_enroll_course_if_course_already_exists_expect_return_correct_string_and_update_the_notes(self):
        expected_return = "Course already added. Notes have been updated."
        expected_notes = ["note1", "note2", "note3"]
        result = self.student.enroll("basic", ["note3"])

        self.assertEqual(expected_return, result)
        self.assertEqual(expected_notes, self.student.courses["basic"])

    def test_enroll_course_if_course_not_in_courses_and_add_course_notes_is_Y_expected_new_course_with_notes(self):
        expected_return = "Course and course notes have been added."
        result = self.student_without_courses.enroll("fund", ["alabala"])

        self.assertEqual(expected_return, result)
        self.assertEqual({"fund": ["alabala"]}, self.student_without_courses.courses)

    def test_enroll_in_new_course_without_third_param_adds_notes_to_the_course(self):
        result = self.student_without_courses.enroll("basic", ["x + y = z"])

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"basic": ["x + y = z"]}, self.student_without_courses.courses)

    def test_enroll_course_without_notes(self):
        expected_return = "Course has been added."
        result = self.student_without_courses.enroll("fund", ["alabala"], "N")

        self.assertEqual(expected_return, result)
        self.assertEqual({"fund": []}, self.student_without_courses.courses)

    def test_add_notes_when_course_name_does_not_exist_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("fund", "alabala")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_correctly_expected_string_return_and_notes_update(self):
        result = self.student.add_notes("basic", "alabala")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["note1", "note2", "alabala"], self.student.courses["basic"])

    def test_leave_course_when_course_does_not_exist_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("fund")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_correctly(self):
        result = self.student.leave_course("basic")

        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)


if __name__ == '__main__':
    main()
