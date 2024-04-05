from django.shortcuts import render
from .models import *


def home(request):
    profile = Profile.objects.filter(user= request.user).first()
    context = {
        'profile': profile
    }
    return render(request, 'home.html',context)
