from django.http import JsonResponse

def test_request(request):
    return JsonResponse({'message': 'testoviy zapros'})
