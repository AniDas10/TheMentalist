from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('signup', views.signupUser, name="signup"),
    path('profile', views.profile, name="profile"),
    path('flappy', views.flappy, name="flappy"),
    path('write', views.write, name="write"),
    path('mind', views.mind, name="mind"),
    path('game', views.game, name="game"),
    path('chatbot', views.chatbot, name="chatbot"),
    path('api/save-score/<int:score>', views.SaveScore.as_view(), name="savescore"),
]