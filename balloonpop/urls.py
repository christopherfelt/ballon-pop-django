from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pop/pop/pop/', admin.site.urls),
    path('', include('game.urls')),
    path('accounts/', include('allauth.urls'))
]
