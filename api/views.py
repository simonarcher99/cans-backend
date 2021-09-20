import json
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

def main(request):

    if request.method == 'GET':
        data = json.dumps({"message": "Connected to backend"})
        return HttpResponse(data, content_type='application/json')
