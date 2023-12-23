from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import PeopleSerializer



@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        json_response = {
            'name':'Scaler',
            'courses':['C++','Python'],
            'method':'GET'
        }
    else:
        data = request.data
        print(data)
        json_response = {
            'name':'Scaler',
            'courses':['C++','Python'],
            'method':'GET'
        }
    return Response(json_response)

    
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.filter(color__isnull=False)
        serializer = PeopleSerializer(objs,many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data = data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({"Response":"Person Deleted "})
    
     

    

