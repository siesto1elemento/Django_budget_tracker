from django.shortcuts import render
from .models import *


def home(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        amount = request.POST.get('amount')
        expense_type = request.POST.get('expense_type')
    
        
    
    
    
    
    
    
    profile = Profile.objects.filter(user= request.user).first()
    context = {
        'profile': profile
    }
    return render(request, 'home.html',context)
