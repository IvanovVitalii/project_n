from django.contrib.auth.models import User
from django.test import TestCase

from posts.models import Post


class ViewsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_user_1 = User.objects.create(username='test_user_1')

    def setUp(self):
        self.post_1 = Post.objects.create(
            title='test_title_1',
            author=self.test_user_1,
            content='test_content_1'
        )

    def test_str_to_title(self):
        post = self.post_1
        self.assertEqual(str(post), post.title)
