from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import request

from account.forms import CustomerUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomerUserCreationForm()
    context = {
        "form":form
    }
    return render(request, 'account/register.html' , context=context)


def profile(request):
    return render(request , 'account/profile.html')