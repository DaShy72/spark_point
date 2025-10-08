from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomAuthenticationForm, CustomUserCreationForm


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm
    return render(request, 'user/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next') or '/'
            return redirect(next_url)
    else:
        form = CustomAuthenticationForm()

    return render(request, 'user/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, 'main_app/index.html')