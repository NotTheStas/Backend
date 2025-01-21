import requests
from django.http import JsonResponse
from django.conf import settings


def redirect_mainapp(request):
    main_server_url = settings.URL_TO_MAIN_SERVER
    response = requests.get(main_server_url)
    response_data = response.json()
    return JsonResponse(response_data)
