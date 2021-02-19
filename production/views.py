from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from production.models import Production
from production.serializers import ProductionSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST'])
def production_list(request):
    if request.method == 'GET':
        production = Production.objects.all()

        name = request.GET.get('name',None)
        if name is not None:
            production = production.filter(name__icontains=name)

        production_serializer = ProductionSerializer(production, many=True)
        return JsonResponse(production_serializer.data, safe=False)

    elif request.method == 'POST':
        production_data = JSONParser().parse(request)
        production_serializer = ProductionSerializer(data = production_data)
        if production_serializer.is_valid():
            production_serializer.save()
            return JsonResponse(production_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(production_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def production_detail(request, pk):
    try:
        production = Production.objects.get(pk=pk)
    except Production.DoesNotExist:
        return JsonResponse({'message':'The note does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        production_serializer = ProductionSerializer(production)
        return JsonResponse(production_serializer.data)

    elif request.method == 'PUT':
        production_data = JSONParser().parse(request)
        production_serializer = ProductionSerializer(production, data=production_data)
        if production_serializer.is_valid():
            production_serializer.save()
            return JsonResponse(production_serializer.data)
        return JsonResponse(production_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        production.delete()
        return JsonResponse({'message':'Production was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
