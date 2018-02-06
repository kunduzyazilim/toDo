# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import *
from .forms import toDoListForm, userLoginForm
from .models import *


@login_required(login_url='/')
def toDo_List(request):
    toDoList_Form = toDoListForm(request.POST or None)
    tasks = Todolist.objects.all()
    act = 'class="checked"'
    context = {
        "PageTitle": "CyprusBooking To-Do-List",
        "form": toDoList_Form,
        "tasks": tasks,
    }
    if toDoList_Form.is_valid():
        print(toDoList_Form.cleaned_data)
    if request.method == "POST":
        if request.POST.get('myform'):
            gorev = request.POST.get('gorev')
            taskAdd = Todolist(todoicerik=gorev, yapildi=0, user_id=request.user.id)
            taskAdd.save()
        if request.GET.get('tasksil'):
            sil = request.POST.get('u')
            taskSil = Todolist.objects.get(id=sil)
            taskSil.delete()
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
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect("/tasks/")
        else:
            hata.append("Kullanıcı adı veya Şifreniz yanlış...")
    return render(request, 'auth/login.html', context)


def logout(request):
    logout(request)
    redirect(request,"/")
