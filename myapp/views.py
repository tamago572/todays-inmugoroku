from django.http import HttpResponse
from django.shortcuts import render
from .forms import GorokuForm
import random
from .models import Goroku

# Create your views here.
def index(request):
    inmugoroku = Goroku.objects.order_by("-created_at")

    emb_variable = {
        "inmugoroku": random.choice(inmugoroku),
        "inmuList": inmugoroku,
        "gorokuForm": GorokuForm(),
        "insertedVar": "",
    }

    if (request.method == "POST"):
        emb_variable["insertedVar"] = request.POST["goroku"]

    return render(request, "myApp/index.html", emb_variable)
