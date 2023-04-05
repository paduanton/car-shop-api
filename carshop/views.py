from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from .models import Car, CarOwner
from .serializers import CarOwnerSerializer, CarSerializer

class CarOwnerView(
    APIView,
    UpdateModelMixin,
    DestroyModelMixin,
):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=None):
        queryset = CarOwner.objects.all()
        read_serializer = CarOwnerSerializer(queryset, many=True)
        car_owners = []

        for car_owner in read_serializer.data:
            cars_queryset = Car.objects.filter(car_owner_id=car_owner["id"])
            cars = CarSerializer(cars_queryset, many=True)

            owner = car_owner
            owner["cars"] = cars.data;
            
            car_owners.append(owner)
        
        return Response(car_owners)

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
    permission_classes = (IsAuthenticated,)

    def get(self, request, owner_id):
        queryset = Car.objects.filter(car_owner_id=owner_id)
        read_serializer = CarSerializer(queryset, many=True)

        return Response(read_serializer.data)

    def post(self, request, owner_id):
        owner_cars = Car.objects.filter(car_owner_id=owner_id)

        if len(owner_cars) == 3:
            return Response({"message": "a person should have up to 3 cars"}, status=400)

        car_data = request.data
        car_data["car_owner_id"] = owner_id

        create_serializer = CarSerializer(data=car_data)

        if create_serializer.is_valid():
            car = create_serializer.save()
            read_serializer = CarSerializer(car)

            return Response(read_serializer.data, status=201)

        return Response(create_serializer.errors, status=400)



