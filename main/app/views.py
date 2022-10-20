from itertools import product
from django.shortcuts import render, redirect
from .serializers import *
from .functions import get_csv_products, handle_uploaded_File
from django.http import HttpResponse
import io
import json
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account created for ' + username)
                return redirect('login')
        context = {'form': form}
        return render(request, 'app/register.html', context)

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is Incorrect')

        context = {}
        return render(request, 'app/login.html', context)

@login_required(login_url='login')
def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        file_obj = FileSerializer(data=request.FILES)
        if file_obj.is_valid():
            file_obj.save()
            a = handle_uploaded_File(str(request.FILES['file']))
            b = get_csv_products(str(request.FILES['file']))
            new_model = resultResponse.objects.create(result_tags=a, user=request.user, product_list=b)
            new_model.save()
            # return redirect('home')
    past_requests = resultResponse.objects.filter(user=request.user).all()
    serialized = ResultSerializer(past_requests)
    print(serialized.data)
    context = {'past_requests': past_requests}
    return render(request, 'app/index.html', context)