from django.urls import path

from .views import BalloonPopHomePage, GameView, SaveScore, LeaderboardView, ProfileView

urlpatterns = [
    path('', BalloonPopHomePage.as_view(), name="homepage"),
    path('game/', GameView.as_view(), name="game"),
    path('savescore/', SaveScore.as_view(), name="savescore"),
    path('leaderboard/', LeaderboardView.as_view(), name="leaderboard"),
    path('profile/', ProfileView.as_view(), name="profile")

]
