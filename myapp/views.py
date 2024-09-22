from django.http import HttpResponse
from django.shortcuts import render
from .forms import GorokuForm
import random

# Create your views here.
def index(request):
    inmugoroku = ["やりますねぇ！", "そうだよ（便乗）", "１１４５１４", "お、そうだな（適当）", "ホラホラホラホラ", "俺らが着替えてるとき、チラチラ見てただろ", "ンアーーーッ！", "810114514931364364", "みろよみろよ", "いいゾ～これ"]

    emb_variable = {
        "inmugoroku": random.choice(inmugoroku),
        "inmuList": inmugoroku,
        "gorokuForm": GorokuForm(),
        "insertedVar": "",
    }

    if (request.method == "POST"):
        emb_variable["insertedVar"] = request.POST["goroku"]

    return render(request, "myApp/index.html", emb_variable)
