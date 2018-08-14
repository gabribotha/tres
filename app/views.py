# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.


def index(request):
    return HttpResponse('Hello World!')


def test(request):
    return HttpResponse('Hello Test!')


def profile(request):
    parsedData = []

    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)

        jsonList = [json.loads(req.content)]

        for data in jsonList:
            parsedData.append({
                'name': data['name'],
                'blog': data['blog'],
                'email': data['email'],
                'public_gists': data['public_gists'],
                'public_repos': data['public_repos'],
                'avatar_url': data['avatar_url'],
                'followers': data['followers'],
                'following': data['following']
            })

    return render(request, 'app/profile.html', {'data': parsedData})
