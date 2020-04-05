from django.urls import path

from .views import BalloonPopHomePage

urlpatterns = [
    path('', BalloonPopHomePage.as_view(), name="homepage")
]
