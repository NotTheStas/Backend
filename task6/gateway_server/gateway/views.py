import requests
from django.http import JsonResponse


def redirect_mainapp(request):

    response = requests.get("http://127.0.0.1:8000")
    response_data = response.json()
    return JsonResponse(response_data)
