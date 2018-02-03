# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import toDoListForm, userLoginForm

@login_required(login_url='auth/login.html')
def toDo_List(request):
    toDoList_Form = toDoListForm(request.POST or None)
    context = {
        "PageTitle": "CyprusBooking To-Do-List",
        "form": toDoList_Form,
    }
    if toDoList_Form.is_valid():
        print(toDoList_Form.cleaned_data)
    if request.method == "POST":
        print(request.POST)
        gorev = request.POST.get('gorev')
        print(gorev)
        hata = []
        if not (gorev):
            hata.append(u'GÖREV GİRMELİSİNİZ !')
        if hata:
            return HttpResponse(u'Eksik Bırakılan Yerleri Düzeltip Yeniden gönderin : %s'.join(hata))
    return render(request, 'todolist.html', context)

def userLogin(request):
    hata = []
    loginForm = userLoginForm(request.POST or None)
    context = {
        "PageTitle": "SIGN-IN",
        "form": loginForm,
        "hata": hata
    }
    if loginForm.is_valid():
        print(loginForm.cleaned_data)
        username = loginForm.cleaned_data.get('usrname')
        password = loginForm.cleaned_data.get('pswd')
        # hatirla = loginForm.cleaned_data.get('remember')
        user = authenticate(request, username=username, password=password)
        print(user)
        print(request.user.is_authenticated)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            return redirect("/tasks")
        else:
            hata.append("Kullanıcı adı veya Şifreniz yanlış...")
    return render(request, 'auth/login.html', context)

def logout(request):
    logout(request)
