from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import Car, CarOwner
from .serializers import CarOwnerSerializer, CarSerializer

class CarOwnerView(
    APIView,
    UpdateModelMixin,
    DestroyModelMixin,
):

    def get(self, request, id=None):
        queryset = CarOwner.objects.all()
        read_serializer = CarOwnerSerializer(queryset, many=True)

        return Response(read_serializer.data)

    def post(self, request):

        create_serializer = CarOwnerSerializer(data=request.data)

        if create_serializer.is_valid():
            car_owner = create_serializer.save()
            read_serializer = CarOwnerSerializer(car_owner)

            return Response(read_serializer.data, status=201)

        return Response(create_serializer.errors, status=400)
    
class CarView(
    APIView,
    UpdateModelMixin,
    DestroyModelMixin,
):

    def get(self, request):
        queryset = CarSerializer.objects.all()
        read_serializer = CarOwnerSerializer(queryset, many=True)

        return Response(read_serializer.data)

    def post(self, request, owner_id):
        car_owner = CarOwner.objects.get(pk=owner_id);
        
        car_data = request.data
        car_data["car_owner"] = car_owner

        create_serializer = CarSerializer(data=request.data)

        if create_serializer.is_valid():
            car = create_serializer.save()
            read_serializer = CarSerializer(car)

            return Response(read_serializer.data, status=201)

        return Response(create_serializer.errors, status=400)



