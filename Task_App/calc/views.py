from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

@api_view(['GET'])
def add_two_numbers(request: Request)->Response:
    print ("Insert Added two numbers")
    a = int(request.GET.get('a'))
    b = int(request.GET.get('b'))

    result = a+b
    return Response({
        'a': a,
        'b': b,
        'result': result
    })