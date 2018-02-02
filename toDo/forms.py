#-*- coding: utf-8 -*-
from django import forms

class toDoListForm (forms.Form):
    gorev = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "id":"myInput",
            "placeholder":"Görev Bilgisi...",
            "name":"gorev",
            'required': False
        })
    )

class userLoginForm (forms.Form):
    userName = forms.CharField(
        label="Kullanıcı Adı : ",
        widget=forms.TextInput(attrs={
            "id":"usrName",
            "class":"form-control",
            "placeholder":"Kullanıcı Adınızı Girin...",
            "name":"usrname",
        })
    )
    passwd = forms.CharField(
        label="Şifre : ",
        widget=forms.PasswordInput(attrs={
            "id":"sifre",
            "class": "form-control",
            "name": "pswd",
        })
    )
    remember = forms.BooleanField(
        label="Beni Hatırla",
        required=False,
        widget=forms.CheckboxInput(attrs={
            "id":"hatirla",
            "class": "form-check-input",
            "name": "remember",
        })
    )