#-*- coding: utf-8 -*-

from django import forms

class toDoListForm (forms.Form):
    gorev = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
               "id":"myInput",
               "placeholder":"Görev Bilgisi...",
               "name":"gorev"})
    )