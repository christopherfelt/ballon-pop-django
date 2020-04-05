from django.urls import path

from .views import BalloonPopHomePage, GameView

urlpatterns = [
    path('', BalloonPopHomePage.as_view(), name="homepage"),
    path('game/', GameView.as_view(), name="game"),
]
