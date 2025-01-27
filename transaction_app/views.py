from django.shortcuts import render
from .models import Transaction


def index(request):
    data = Transaction.objects.all().values()
    return render(request,"index.html",{"transactions":data})
