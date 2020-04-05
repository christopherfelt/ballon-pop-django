from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class BalloonPopHomePage(TemplateView):
    template_name = "home.html"


class GameView(LoginRequiredMixin, TemplateView):
    login_redirect_field = "account_login"
    template_name = "game.html"



