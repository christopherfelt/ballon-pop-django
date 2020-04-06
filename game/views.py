from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.db.models import Max

from .models import Score

class BalloonPopHomePage(TemplateView):
    template_name = "home.html"


class GameView(LoginRequiredMixin, TemplateView):
    login_redirect_field = "account_login"
    template_name = "game.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['scores'] = Score.objects.filter(user=user).values('score')
        context['highscore'] = Score.objects.filter(user=user).aggregate(Max('score'))['score__max']
        return context
    


