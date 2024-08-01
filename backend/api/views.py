import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    #request.body
    #request -> HttpRequest -> django
    print(request.GET)
    return JsonResponse({"message": "Hello, monkey!"})