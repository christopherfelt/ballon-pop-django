from django.contrib import admin
from .models import Score


class ScoreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Score, ScoreAdmin)
