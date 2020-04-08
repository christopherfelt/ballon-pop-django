from django.views.generic import TemplateView, View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max
from django.http import JsonResponse

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


class SaveScore(View):

    def post(self, request):

        game_score = request.POST['score']

        try: 
            score = Score.objects.create(
                user=request.user,
                score=game_score
            )
            score.save()
            response = {
                'status': 1,
                'message': 'Score saved'
            }
            
        except Exception as e:
            response = {
                'status': 0,
                'message': 'Somthing went wrong - ' + str(e)
            }

        return JsonResponse(response)


class LeaderboardView(ListView):
    template_name = "leaderboard.html"
    model = Score
    queryset = Score.objects.order_by('-score')[:9]
    context_object_name = "scores"


class ProfileView(LoginRequiredMixin, ListView):
    login_redirect_field = "account_login"
    template_name = "profile.html"
    model = Score
    context_object_name = "scores"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
