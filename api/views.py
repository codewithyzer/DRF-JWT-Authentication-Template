from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def token_view(request):
    return JsonResponse({'testing': True, 'token_view': True})

def token_refresh_view(request):
    return JsonResponse({'testing': True, 'token_refresh_view': True})
    
