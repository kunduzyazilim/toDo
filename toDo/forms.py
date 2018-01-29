from django import forms

class toDoListForm (forms.Form):
    gorev = forms.CharField(widget=forms.TextInput(
        attrs={"id":"myInput",
               "placeholder":"Görev Bilgisi...",
               "name":"gorev"}
    )
    )