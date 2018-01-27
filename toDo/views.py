from django.http import HttpResponse
from django.shortcuts import render
from .forms import toDoListForm,gonder

def toDo_List(request):
    toDoList_Form = toDoListForm()
    context = {
        "PageTitle":"CyprusBooking To-Do-List",
        "form": toDoList_Form
    }
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get('gorev'))
    return render(request,'index.html',context)

def indexJs(request):
    return render(request,'index.js',{})

def styleCss(request):
    return render(request,'style.css',{})