from django import forms

class GorokuForm(forms.Form):
    goroku = forms.CharField(label="語録")
    num = forms.IntegerField(label="評価")
