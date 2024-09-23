from django import forms
from .models import Goroku

class GorokuForm(forms.ModelForm):
    class Meta:
        model = Goroku

        fields = ["goroku", "author", "age", "created_at", ]
        labels = {"goroku": "語録", "author": "人物", "age": "年齢を教えてくれるかな", "created_at": "作成日時", }
