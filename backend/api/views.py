from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import persistence
import json

def goals(request):
    if request.method == "GET":
        try:
            data = persistence.read_goals()
            return JsonResponse({"message": data}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Response contains invalid JSON"}, status=400)
        pass
    elif request.method == "POST":
        try:
            data = request.body
            persistence.write_goal(data)
            return JsonResponse({"message": "Successfully created goal"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Response contains invalid JSON"}, status=400)
    elif request.method == "PUT":
        try:
            data = request.body
            persistence.update_goal(data)
            return JsonResponse({"message": "Update goal"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Response contains invalid JSON"}, status=400)
