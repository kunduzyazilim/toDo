# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import *
from .forms import toDoListForm, userLoginForm
from .models import *


# from django.views.generic.edit import DeleteView
# from django.urls import reverse_lazy

@login_required(login_url='/')
def toDo_List(request):
    toDoList_Form = toDoListForm(request.POST or None)
    tasks = Todolist.objects.all()
    user = request.user
    hata = []
    context = {
        "PageTitle": "CyprusBooking To-Do-List",
        "form": toDoList_Form,
        "tasks": tasks.order_by("yapildi", "-date_islenis"),
        "hata": hata,
    }
    if toDoList_Form.is_valid():
        if request.method == "POST":
            gorev = toDoList_Form.cleaned_data.get('gorev')
            taskAdd = Todolist(todoicerik=gorev, yapildi=0, username_id=user.id)
            taskAdd.save()
            if not (gorev):
                hata.append(u'GÖREV GİRMELİSİNİZ !')
            if hata:
                return HttpResponse(u'Eksik Bırakılan Yerleri Düzeltip Yeniden gönderin : %s'.join(hata))
    return render(request, 'todolist.html', context)


# class task_sil(DeleteView):
#         model = Todolist
#         success_url = reverse_lazy('Todolist')

def userLogin(request):
    hata = []
    loginForm = userLoginForm(request.POST or None)
    context = {
        "PageTitle": "SIGN-IN",
        "form": loginForm,
        "hata": hata
    }
    if loginForm.is_valid():
        username = loginForm.cleaned_data.get('usrname')
        password = loginForm.cleaned_data.get('pswd')
        # hatirla = loginForm.cleaned_data.get('remember')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/tasks/")
        else:
            hata.append("Kullanıcı adı veya Şifreniz yanlış...")
    if request.user.is_active:
        return redirect("/tasks/")
    return render(request, 'auth/login.html', context)


def logout_task(request):
    logout(request)
    return redirect("/")
