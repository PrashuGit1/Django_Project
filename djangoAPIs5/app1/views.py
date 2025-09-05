from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def post_data(req):
    if req.method =='POST':
        data = json.loads(req.body)
        print(data)
    return JsonResponse({'message': 'POST data received'}, status=201)

def get_data(req):
    if req.method == 'GET':
        return JsonResponse({'message': 'This is a GET request'}, status=200)


