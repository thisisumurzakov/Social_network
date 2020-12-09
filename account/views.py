from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from  django.contrib.auth.decorators import login_required

from .forms import LoginForm

@login_required()
def dashboard(requst):
    return render(requst, 'account/main.html', {'section': 'dashboard'})

def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    return render(request, 'account/login.html', {'form': form})