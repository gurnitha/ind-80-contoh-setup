# app/main/views.py

# Modul Django
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def halodunia(request):
    now = datetime.datetime.now()
    html = "Halo Dunia!<br> Waktu Jakarta sekarang adalah %s." % now
    return HttpResponse(html)