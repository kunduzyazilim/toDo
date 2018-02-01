#-*- coding: utf-8 -*-
from django.http import *
from django.shortcuts import render
from .forms import toDoListForm,userLoginForm

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
        gorev=request.POST.get('gorev')
        print(gorev)
        hata=[]
        if not (gorev):
            hata.append(u'GÖREV GİRMELİSİNİZ !')
        if hata:
            return HttpResponse(u'Eksik Bırakılan Yerleri Düzeltip Yeniden gönderin : %s'.join(hata))

    return render(request,'index.html',context)

def userLogin(request):
    loginForm = userLoginForm (request.POST or None)
    context = {
        "PageTitle": "CyprusBooking To-Do-List",
        "form": loginForm,
    }
    if loginForm.is_valid():
        print(loginForm.cleaned_data)
    if request.method == "POST":
        print(request.POST)
        usrname=request.POST.get('usrname')
        pswd = request.POST.get('pswd')
        print(usrname,pswd)
        hata=[]
        if not (usrname,pswd):
            hata.append(u'Giriş Yapmak İçin lütfen kullanıcı adı ve şifrenizi giriniz !')
        if hata:
            return HttpResponse(u'Kullanıcı adı veya şifreyi boş bıraktınız : %s'.join(hata))
    return render(request, 'login.html', context)