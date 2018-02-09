# -*- coding: utf-8 -*-
from django import forms


class toDoListForm(forms.Form):
    gorev = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            "id": "myInput",
            "placeholder": "Görev Bilgisi...",
            "name": "gorev",
            "class": "form-control",
            'required': False
        })
    )


class userLoginForm(forms.Form):
    usrname = forms.CharField(
        label="Kullanıcı Adı : ",
        widget=forms.TextInput(attrs={
            "id": "userName",
            "class": "form-control",
            "placeholder": "Kullanıcı Adınızı Girin...",
            "name": "usrname",
        })
    )
    pswd = forms.CharField(
        label="Şifre : ",
        widget=forms.PasswordInput(attrs={
            "id": "sifre",
            "class": "form-control",
            "name": "pswd",
        })
    )

    # remember = forms.BooleanField(
    #     label="Beni Hatırla",
    #     required=False,
    #     widget=forms.CheckboxInput(attrs={
    #         "id":"hatirla",
    #         "class": "form-check-input",
    #         "name": "remember",
    #     })
    # )
