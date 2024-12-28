from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

@login_required
def post_create(request):
    current_user=request.user
    if request.method=='POST':
            form=PostCreateForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                  post = form.save(commit=False)
                  post.user = request.user
                  post.save(commit=True)
    else:
          form=PostCreateForm()
    return render(request, 'posts/create.html', {'form':form, 'current_user':current_user})