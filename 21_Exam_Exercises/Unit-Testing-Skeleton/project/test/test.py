from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self) -> None:
        self.social_media = SocialMedia("kris", "Instagram", 10000, "cars")

    def test_correct_init(self):
        self.assertEqual("kris", self.social_media._username)
        self.assertEqual("Instagram", self.social_media._platform)
        self.assertEqual(10000, self.social_media.followers)
        self.assertEqual("cars", self.social_media._content_type)

    def test_init_with_invalid_platform_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.platform = "asdasd"

        self.assertEqual("Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(ve.exception))

    def test_init_with_negative_followers_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -12

        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test_create_post_expected_success(self):
        expected_message = "New cars post created by kris on Instagram."
        expected_post = [{'content': "new cars", 'likes': 0, 'comments': []}]

        result = self.social_media.create_post("new cars")

        self.assertEqual(expected_message, result)
        self.assertEqual(expected_post, self.social_media._posts)

    def test_like_post_success_added_likes_to_post_with_post_index(self):
        new_post = {'content': "new cars", 'likes': 0, 'comments': []}
        self.social_media._posts.append(new_post)

        result = self.social_media.like_post(0)

        self.assertEqual("Post liked by kris.", result)
        self.assertEqual(1, self.social_media._posts[0]["likes"])

    def test_like_post_when_post_reached_maximum_of_10_likes(self):
        new_post = {'content': "new cars", 'likes': 10, 'comments': []}
        self.social_media._posts.append(new_post)

        result = self.social_media.like_post(0)

        self.assertEqual("Post has reached the maximum number of likes.", result)
        self.assertEqual(10, self.social_media._posts[0]["likes"])

    def test_like_post_when_is_given_invalid_post_index(self):
        new_post = {'content': "new cars", 'likes': 10, 'comments': []}
        self.social_media._posts.append(new_post)

        result = self.social_media.like_post(5)

        self.assertEqual("Invalid post index.", result)

    def test_comment_on_post_with_more_then_10_chars_expected_success(self):
        new_post = {'content': "new cars", 'likes': 5, 'comments': []}
        self.social_media._posts.append(new_post)

        result = self.social_media.comment_on_post(0, "I like your posts!")

        self.assertEqual("Comment added by kris on the post.", result)
        self.assertEqual([{'user': "kris", 'comment': "I like your posts!"}],
                         self.social_media._posts[0]["comments"])

    def test_comment_on_post_with_short_comment(self):
        new_post = {'content': "new cars", 'likes': 5, 'comments': []}
        self.social_media._posts.append(new_post)

        result = self.social_media.comment_on_post(0, "nice")

        self.assertEqual("Comment should be more than 10 characters.", result)








if __name__ == '__main':
    main()