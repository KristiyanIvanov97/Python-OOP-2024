from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("me", 1, 100, 100)
        self.enemy_hero = Hero("you", 1, 50, 50)

    def test_correct_init(self):
        self.assertEqual("me", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_when_enemy_hero_has_the_same_username_as_hero(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_when_health_is_below_or_equal_to_zero_raise_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_when_enemy_hero_health_is_below_or_equal_to_zero_raise_value_error(self):
        self.enemy_hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ve.exception))

    def test_fight_enemy_and_win_increase_stats(self):
        expected_level = self.hero.level + 1
        expected_damage = self.hero.damage + 5
        expected_health = self.hero.health - self.enemy_hero.damage + 5

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual("You win", result)
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)

    def test_fight_with_result_draw_return_draw_and_decrease_both_stats(self):
        self.hero.health = 50

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual("Draw", result)
        self.assertEqual(-50, self.enemy_hero.health)
        self.assertEqual(0, self.hero.health)

    def test_fight_enemy_and_lose_expect_enemy_stats_increase(self):
        self.hero, self.enemy_hero = self.enemy_hero, self.hero

        expected_level = self.enemy_hero.level + 1
        expected_damage = self.enemy_hero.damage + 5
        expected_health = self.enemy_hero.health - self.hero.damage + 5

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual("You lose", result)
        self.assertEqual(expected_level, self.enemy_hero.level)
        self.assertEqual(expected_health, self.enemy_hero.health)
        self.assertEqual(expected_damage, self.enemy_hero.damage)

    def test_correct__str__(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                          f"Health: {self.hero.health}\n" \
                          f"Damage: {self.hero.damage}\n"

        self.assertEqual(expected_result, str(self.hero))

if __name__ == '__main':
    main()
