from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status

from toys.models import Toy
from toys.serializers import ToySerializer


# class JSONResponse(HTTPResponse):
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)
#         return data


@csrf_exempt
def toy_list(request):
    if request.method == 'GET':
        toys = Toy.objects.all()
        toys_serialzier = ToySerializer(toys, many=True)
        return JsonResponse(toys_serialzier.data, safe=False)
    
    elif request.method == 'POST':
        toy_data = JSONParser().parse(request)
        toy_serailizer = ToySerializer(data=toy_data)
        if toy_serailizer.is_valid():
            toy_serailizer.save()
            return JsonResponse(toy_serailizer.data, status=status.HTTP_201_CREATED)
        print(toy_serailizer.errors)
        return JsonResponse(toy_serailizer.errors, status=status.HTTP_400_BAD_REQUEST)


    
@csrf_exempt
def toy_detail(request, pk):
    try:
        toy = Toy.objects.get(pk=pk)
    except Toy.DoesNotExist:
        return JsonResponse({"message": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        toy_serializer = ToySerializer(toy)
        return JsonResponse(toy_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        toy_data = JSONParser().parse(request)
        toy_serializer = ToySerializer(toy, data=toy_data)
        if toy_serializer.is_valid():
            toy_serializer.save()
            return JsonResponse(toy_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(toy_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        toy.delete()
        return HTTPResponse(status=status.HTTP_204_NO_CONTENT)