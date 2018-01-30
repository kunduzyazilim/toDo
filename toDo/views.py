#-*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from .forms import toDoListForm

def toDo_List(request):
    toDoList_Form = toDoListForm(request.POST or None)
    context = {
        "PageTitle": "CyprusBooking To-Do-List",
        "form": toDoList_Form,
    }
    if toDoList_Form.is_valid():
        print(toDoList_Form.cleaned_data)
    if request.method == "POST":
        print(request.POST.get('gorev'))
    return render(request,'index.html',context)