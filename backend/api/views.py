from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import persistence

def goals(request):
    body = request.body
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return JsonResponse({"message": "Request contains invalid JSON"}, status=400)

    if request.method == "GET":
        try:
            json.loads(persistence.read_goals())
            return JsonResponse({"message": "Read goal"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Response contains invalid JSON"}, status=400)
        pass
    elif request.method == "POST":
        try:
            json.loads(persistence.write_goal())
            return JsonResponse({"message": "Wrote goal"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Response contains invalid JSON"}, status=400)
    elif request.method == "PUT":
        try:
            json.loads(persistence.update_goal())
            return JsonResponse({"message": "Update goal"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Response contains invalid JSON"}, status=400)
