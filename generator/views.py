from django.shortcuts import render
import random
import string

def home(request):
    return render(request, "generator/home.html")

def about(request):
    return render(request, "generator/about.html")

def password(request):
    characters = []
    for i in range(97,123):
        characters.append(chr(i))

    if request.GET.get('uppercase'):
        characters.extend([j.upper() for j in characters])

    if request.GET.get('special'):
        characters.extend(string.punctuation)

    if request.GET.get('numbers'):
        characters.extend(string.digits)

    length = request.GET.get('length')
    password = ''
    for x in range(int(length)):
        password+=random.choice(characters)
    return render(request, "generator/password.html", {'password':password})
