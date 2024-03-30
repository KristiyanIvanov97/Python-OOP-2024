from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("me", 3, 100, 50)
        self.enemy_hero = Hero("you", 2, 50, 10)

    def test_correct_init(self):
        self.assertEqual("me", self.hero.username)
        self.assertEqual("you", self.enemy_hero.username)
        self.assertEqual(3, self.hero.level)
        self.assertEqual(2, self.enemy_hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(50, self.enemy_hero.health)
        self.assertEqual(50, self.hero.damage)
        self.assertEqual(10, self.enemy_hero.damage)

    def test_battle_when_enemy_hero_has_the_same_username_as_hero(self):
        self.enemy_hero.username = self.hero.username

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_when_health_is_below_or_equal_to_zero_raise_value_error(self):
        self.hero.health = 0

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_when_enemy_hero_health_is_below_or_equal_to_zero_raise_value_error(self):
        self.enemy_hero.health = 0

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ex.exception))

    def test_fight_enemy_and_win_increase_stats(self):
        expected_health = self.hero.health - self.enemy_hero.damage + 5
        expected_level = self.hero.level + 1
        expected_damage = self.hero.damage + 5

        result = self.hero.battle(self.enemy_hero)

        self.assertEquals("You win", result)
        self.assertEquals(expected_health, self.hero.health)
        self.assertEquals(expected_level, self.hero.level)
        self.assertEquals(expected_damage, self.hero.damage)


if __name__ == '__main':
    main()
