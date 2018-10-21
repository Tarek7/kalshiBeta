from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from bets.core.forms import SignUpForm
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the questions index.")

def Question(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def MyBets(request, user_id):
    response = "You're looking at user: %s."
    return HttpResponse(response % user_id)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.wallet_number = form.cleaned_data.get('wallet_number')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
