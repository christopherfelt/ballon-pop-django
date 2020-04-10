from django.test import SimpleTestCase
from django.urls import reverse, resolve

from game.views import (BalloonPopHomePage, GameView, SaveScore,
                        LeaderboardView, ProfileView)


class TestUrls(SimpleTestCase):

    def test_homepage_url_resolves(self):
        url = reverse('homepage')
        self.assertEquals(resolve(url).func.view_class, BalloonPopHomePage)

    def test_game_url_resolves(self):
        url = reverse('game')
        self.assertEquals(resolve(url).func.view_class, GameView)

    def test_savescore_url_resolves(self):
        url = reverse('savescore')
        self.assertEquals(resolve(url).func.view_class, SaveScore)

    def test_leaderboard_url_resolves(self):
        url = reverse('leaderboard')
        self.assertEquals(resolve(url).func.view_class, LeaderboardView)

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func.view_class, ProfileView)
