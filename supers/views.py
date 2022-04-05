from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Supers
from supers import serializers

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        supers = Supers.objects.all()
        serializers = SuperSerializer(supers, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
     
@api_view(['GET'])
def supers_detail(request, pk):
    try:
        super = Supers.objects.get(pk=pk)
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    except Supers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

