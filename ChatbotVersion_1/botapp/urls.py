from django.urls import path
from .views import bot

urlpatterns = [
    path('bot/<Question>', bot.as_view(), name='bot'),
]
