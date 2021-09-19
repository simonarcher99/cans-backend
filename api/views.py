from django.shortcuts import render
from django.http import JsonResponse


def main(request):
    return JsonResponse({'status': 200, 'content': 'Succesfully connected to backend'})
