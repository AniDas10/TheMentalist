from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils.html import escape

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.utils.html import escape
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework import generics, status
from Ani import report, classifyProblem
from .models import *


def index(request):
    return HttpResponse("Welcome!")

def signupUser(request):
    if request.method == 'POST':
        username = escape(request.POST['username'])
        raw_password = escape(request.POST['password1'])
        raw_password2 = escape(request.POST['password2'])
        try:
            if raw_password == raw_password2 and len(raw_password) >= 6:
                user = User.objects.create(username=username, password=raw_password)
                user.set_password(raw_password)
                user.save()
                login(request, user) # logs User in
                session = Session.objects.create(user=user)
                UserMetaData.objects.create(user=user, current_session=session)
                return redirect('home')
            elif len(raw_password) >= 6:
                return render(request, 'Authentication/signup.html', {'error': "Passwords do not match!"})
            else:
                return render(request, 'Authentication/signup.html', {'error': "Password must be 6 characters or more"})
        except Exception as e:
            return render(request, 'Authentication/signup.html', {'error': str(e)})
    return render(request, 'Authentication/signup.html', {'error': None})

def loginUser(request):
    if request.method == 'POST':
        username = escape(request.POST['username'])
        raw_password = escape(request.POST['password'])
        user = authenticate(username=username, password=raw_password)
        if user is not None:
            login(request, user) # logs User in
            return redirect('home')
        else:
            return render(request, 'Authentication/signup.html', {'error': "Unable to Log you in!"})
    return render(request, 'Authentication/login.html', {'error': None})

def logoutUser(request):
    logout(request)
    return redirect('index')

@login_required
def home(request):
    return HttpResponse("your dashboard")

@login_required
def flappy(request):
    return render(request, 'flappy.html')

@login_required
def chat(request):
    user = request.user
    meta = UserMetaData.objects.get(user=user)
    if request.method == 'POST':
        ans = request.POST['answer']
        game = Game.objects.get(id=request.POST['gid'])
        game.answer = ans
        game.save()
        q_no = Game.objects.filter(session=meta.current_session).count()
        if meta.current_session.count < 3:
            keyword = 'intro'
        else:
            keyword = meta.disorder
        if q_no == report.get_session_question_count(keyword, meta.current_session.count):
            if meta.current_session.count == 1:
                new_session = Session.objects.create(user=user, count=2)
                meta.current_session = new_session
            elif meta.current_session.count == 2:
                games = Game.objects.filter(session=meta.current_session)
                meta.disorder = classifyProblem.classify(games.values_list('answer', flat=True))
                meta.save()
                new_session = Session.objects.create(user=user, count=3)
                meta.current_session = new_session
            else:
                curr = meta.current_session
                curr.result, curr.result_percent = report.analysis_per_session()
                curr.save()
                new_session = Session.objects.create(user=user, count=curr.count+1)
                meta.current_session = new_session
            meta.save()
    games = Game.objects.filter(session__user=request.user).exclude(answer__isnull=True)
    try:
        last_game = Game.objects.get(session=meta.current_session, answer=None)
        return render(request, 'chat.html', {'new_question': last_game.question, 'gid': last_game.id, 'games': games})
    except Exception:
        return render(request, 'chat.html', {'games': games})


class SaveScore(generics.GenericAPIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        user = request.user
        meta = UserMetaData.objects.get(user=user)
        if meta.current_session.count < 3:
            keyword = 'intro'
        else:
            keyword = meta.disorder
        q_no = Game.objects.filter(session=meta.current_session).count()
        game_record = Game.objects.create(
            session=meta.current_session,
            score=kwargs['score'],
            question=report.get_next_question(keyword, meta.current_session.count, q_no)
        )
        q_no += 1

        return JsonResponse({"success": True})