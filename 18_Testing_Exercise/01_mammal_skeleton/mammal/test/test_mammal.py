from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal("Stamat", "kotarak", "meow")

    def test_correct_init(self):
        self.assertEqual("Stamat", self.mammal.name)
        self.assertEqual("kotarak", self.mammal.type)
        self.assertEqual("meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_correct_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound_return_correct_string(self):
        self.assertEqual("Stamat makes meow", self.mammal.make_sound())

    def test_info_return_correct_string(self):
        self.assertEqual("Stamat is of type kotarak", self.mammal.info())


if __name__ == '__main__':
    main()
