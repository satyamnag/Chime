from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import *
from posts.models import *

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                return render(request, 'app_users/invalid_credentials.html')
    else:
        form=LoginForm()
    return render(request, 'app_users/login.html', {'form':form})

@login_required
def index(request):
    current_user=request.user
    # posts=Post.objects.filter(user=current_user)
    profile=Profile.objects.all().first()
    # profile=Profile.objects.filter(user=current_user).first()
    posts=Post.objects.all()
    return render(request, 'app_users/index.html', {'posts':posts, 'profile':profile, 'current_user':current_user})

def register(request):
    if request.method == 'POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'app_users/register_done.html')
    else:
        user_form=UserRegistrationForm()
    return render(request, 'app_users/register.html', {'user_form':user_form})

@login_required
def edit(request):
    current_user=request.user
    if request.method=='POST':
        user_form=UserEditForm(instance=request.user, data=request.POST)
        profile_form=ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request, 'app_users/edit_done.html', {'current_user':current_user})
    else:
        user_form=UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)
    return render(request, 'app_users/edit.html', {'user_form':user_form, 'profile_form':profile_form, 'current_user':current_user})


def tnc(request):
    return render(request, 'app_users/tnc.html')

def pp(request):
    return render(request, 'app_users/pp.html')