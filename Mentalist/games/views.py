from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils.html import escape

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.utils.html import escape
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework import generics, status
from Ani import report, classifyProblem, get_emotion
from .models import *
import datetime


def index(request):
    return render(request, 'Frontend/index.html')

def signupUser(request):
    if request.method == 'POST':
        username = escape(request.POST['username'])
        raw_password = escape(request.POST['password'])
        raw_password2 = escape(request.POST['confirm_password'])
        try:
            if raw_password == raw_password2 and len(raw_password) >= 6:
                user = User.objects.create(username=username, password=raw_password)
                user.set_password(raw_password)
                user.save()
                login(request, user) # logs User in
                session = Session.objects.create(user=user)
                UserMetaData.objects.create(user=user, current_session=session)
                return redirect('profile')
            elif len(raw_password) >= 6:
                return render(request, 'Frontend/register.html', {'error': "Passwords do not match!"})
            else:
                return render(request, 'Frontend/register.html', {'error': "Password must be 6 characters or more"})
        except Exception as e:
            return render(request, 'Frontend/register.html', {'error': str(e)})
    return render(request, 'Frontend/register.html', {'error': None})

def loginUser(request):
    if request.method == 'POST':
        username = escape(request.POST['username'])
        raw_password = escape(request.POST['password'])
        user = authenticate(username=username, password=raw_password)
        if user is not None:
            login(request, user) # logs User in
            return redirect('profile')
        else:
            return render(request, 'Frontend/login.html', {'error': "Unable to Log you in!"})
    return render(request, 'Frontend/login.html', {'error':''})

def logoutUser(request):
    logout(request)
    return redirect('index')

@login_required
def profile(request):
    user = request.user
    meta = UserMetaData.objects.get(user=user)
    if request.method == 'POST':
        ans = request.POST['answer']
        game = Game.objects.get(id=request.POST['gid'])
        game.answer = ans
        game.answered_time = datetime.datetime.now()
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
                meta.disorder = classifyProblem.classify([int(v) for v in games.values_list('answer', flat=True)])
                meta.save()
                new_session = Session.objects.create(user=user, count=3)
                meta.current_session = new_session
            else:
                curr = meta.current_session
                games = Game.objects.filter(session=curr)
                curr.result, curr.result_percent = report.analysis_per_session([int(v) for v in games.values_list('answer', flat=True)])
                curr.save()
                new_session = Session.objects.create(user=user, count=curr.count+1)
                meta.current_session = new_session
            meta.save()
    games = Game.objects.filter(session=meta.current_session).exclude(answer__isnull=True)
    result_percentages = [float(v) for v in Session.objects.filter(user=user, count__gte=3).values_list('result_percent', flat=True) if v]
    growth_sessions = []
    growth_rates = []
    for session in Session.objects.filter(user=user):
        sesh_games = Game.objects.filter(session=session)
        growth_sessions.append(session.count)
        growth_rates.append(report.game_score_analysis(list(sesh_games.values_list('score', flat=True))))
    while len(result_percentages) < 3:
        result_percentages.append(0.0)
    try:
        last_game = Game.objects.filter(session=meta.current_session, answer=None).first()
        return render(request, 'Frontend/profile.html', {'last_game': last_game, 'games': games, 'meta': meta, 'session': meta.current_session, 'result_percentages': result_percentages, 'growth_sessions': growth_sessions, 'growth_rates': growth_rates})
    except Exception:
        return render(request, 'Frontend/profile.html', {'games': games, 'meta': meta, 'session': meta.current_session, 'result_percentages': result_percentages, 'growth_sessions': growth_sessions, 'growth_rates': growth_rates})

@login_required
def flappy(request):
    return render(request, 'flappy.html')

@login_required
def write(request):
    if request.method == 'POST':
        entry = MindJournalEntry()
        entry.user = request.user
        entry.question1 = escape(request.POST['question1'])
        entry.question2 = escape(request.POST['question2'])
        entry.question3 = escape(request.POST['question3'])
        entry.question4 = escape(request.POST['question4'])
        entry.question5 = escape(request.POST['question5'])
        entry.question6 = escape(request.POST['question6'])
        entry.emotion = get_emotion.get_emotion(entry.question1+'.'+entry.question2+'.'+entry.question3+'.'+entry.question4+'.'+entry.question5+'.'+entry.question6)
        entry.save()
        return redirect('mind')
    return render(request, 'Frontend/write.html', {'error':''})

@login_required
def mind(request):
    entries = MindJournalEntry.objects.filter(user=request.user).order_by('timestamp')
    return render(request, 'Frontend/journal.html', {'entries': entries})

@login_required
def game(request):
    return render(request, 'Frontend/game.html')

@login_required
def chatbot(request):
    return render(request, 'Frontend/chatbot.html')


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