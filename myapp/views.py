from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import GorokuForm
import random
from .models import Goroku

# Create your views here.

def index(request):
    inmugoroku = Goroku.objects.order_by("-created_at")

    emb_variable = {
        "page_title": "トップ",
        "inmugoroku": random.choice(inmugoroku),
        "inmuList": inmugoroku,
        "gorokuForm": GorokuForm(),
    }

    # リクエストがPOSTの場合
    if (request.method == "POST"):
        form = GorokuForm(request.POST)
        # バリデーションのチェック
        if form.is_valid():
            # DBに保存 GorokuForm(request.POST)だからおｋということらしい
            form.save()

            # GET indexにリダイレクト
            return redirect("index")

    # ページをレンダリング
    return render(request, "myApp/index.html", emb_variable)

