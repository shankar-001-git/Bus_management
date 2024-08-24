from django.shortcuts import render
from busapp.models import BusDetails
from busapp.serializer import BusDetailsSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def index(request):
    if request.method=='GET':
        buses=BusDetails.objects.all()
        bus_data=BusDetailsSerializer(buses,many=True)
        return JsonResponse(bus_data.data,safe=False)

    elif request.method == 'POST':
        buses = JsonResponse().parse(request)
        busseserializer = BusDetailsSerializer(data=buses)
        if busseserializer.is_valid():
            busseserializer.save()
            return JsonResponse("Data added sucessfully",safe=False)
    
    elif request.method == 'PUT':
        buses = JSONParser().parse(request)
        bus_data = BusDetails.objects.get(id=buses['id'])
        busseserializer = BusDetailsSerializer(bus_data,data = buses)
        if busseserializer.is_valid():
            busseserializer.save()
            return JsonResponse("Data updated sucesfully",safe=False)       
    
    elif request.method == 'DELETE':
        bus_data = BusDetails.objects.get(id=id)
        bus_data.delete()
        return JsonResponse("Data Deleted",safe=False)
@csrf_exempt
def save_file(request):
    files = request.FILES['file']
    file_name = default_storage.save(files.name,files)
    return JsonResponse(file_name,safe=False)

