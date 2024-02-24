from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from . import persistence

def goals(request):
    if request.method == "GET":
        goals = persistence.read_goals()
        return JsonResponse({"message": goals}, status=400)
    elif request.method == "POST":
        pass
    elif request.method == "PUT":
        pass
