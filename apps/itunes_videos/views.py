# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import requests

# Create your views here.
def index(request):
    return render(request, "itunes_videos/index.html")

def search(request):
    if request.method != "POST":
        return redirect(index)
    artist = request.POST["artist"].replace(" ", "")
    url = "https://itunes.apple.com/search?term=" + artist + "&entity=musicVideo"
    response = requests.get(url).content
    return HttpResponse(response, content_type="application/json")