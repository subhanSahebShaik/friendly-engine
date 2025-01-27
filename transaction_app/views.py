from django.shortcuts import render
from .models import Transaction

def index(request):
    data = Transaction.objects.all()
    return render(request,"index.html",{"data":data})