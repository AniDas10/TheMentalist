from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('signup', views.signupUser, name="signup"),
    path('home', views.home, name="home"),
    path('flappy', views.flappy, name="flappy"),
    path('api/save-score/<int:score>', views.SaveScore.as_view(), name="savescore"),
]