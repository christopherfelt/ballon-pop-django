from django.test import TestCase
from django.contrib.auth import get_user_model

from game.models import Score


class TestModels(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="johnsmith1",
            email="johnsmith1@email.com",
            password="testpass123"
        )

        self.score = Score.objects.create(
            user=self.user,
            score=99
        )

    def test_score_creation(self):
        self.assertEqual(f'{self.score.user.username}', 'johnsmith1')
        self.assertEqual(f'{self.score.score}', '99')
        self.assertTrue(self.score.game_datetime)
