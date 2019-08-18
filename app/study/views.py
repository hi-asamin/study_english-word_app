from django.http.response import JsonResponse

import json

def index(request):
    return JsonResponse({'message':'hello study'})
