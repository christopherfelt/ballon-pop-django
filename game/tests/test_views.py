from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
import json

from game.models import Score


class TestViews(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="johnsmith1",
            email="johnsmith1@email.com",
            password="testpass123"
        )
        self.client = Client()
        self.client.login(username="johnsmith1", password="testpass123")
        self.homepage_url = reverse('homepage')
        self.game_url = reverse('game')
        self.savescore_url = reverse('savescore')
        self.leaderboard_url = reverse('leaderboard')
        self.profile_url = reverse('profile')

    def test_login(self):
        self.assertTrue(self.client.login)
        
    def test_homepage_GET(self):
        response = self.client.get(self.homepage_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_game_GET(self):
        response = self.client.get(self.game_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'game.html')

    def test_savescore_POST_new_score(self):

        response = self.client.post(self.savescore_url, {
            'score': '99',
            'user': 'JohnSmith1'
        })

        json_response = json.loads(response.content)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(json_response['message'], "Score saved")

        test_score = Score.objects.all()[0]
        self.assertEquals(test_score.user.username, "johnsmith1")
        self.assertEquals(test_score.score, 99)

    def test_leaderboard_GET(self):
        response = self.client.get(self.leaderboard_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'leaderboard.html')

    def test_profile_GET(self):
        response = self.client.get(self.profile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')