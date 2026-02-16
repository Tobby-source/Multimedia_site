from django.shortcuts import render
from .models import Media

from django.shortcuts import render
from .models import Media  # replace with your actual model

def media_list(request):
    media = Media.objects.all()  # get all media items
    return render(request, 'mediaapp/media_list.html', {'media': media})
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Media

# Home view (example)
def home(request):
    media = Media.objects.all()
    return render(request, 'mediaapp/home.html', {'media': media})

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'mediaapp/signup.html', {'form': form})
