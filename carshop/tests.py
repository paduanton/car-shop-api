from django.core.exceptions import ValidationError
from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Car, CarOwner
from django.contrib.auth.models import User


class TestCarOwnerModel(TestCase):

    def test_create(self):
        try:
            car_owner = CarOwner.objects.create(
                name="Antonio"
            )
            car_owner.save()
        except ValidationError:
            self.fail()

        else:
            self.assertIsInstance(car_owner, CarOwner)
            self.assertEqual(car_owner.name, 'Antonio')


class TestCarModel(TestCase):

    def test_create(self):
        try:
            car_owner = CarOwner.objects.create(
                name="Antonio"
            )
            car_owner.save()

            car = Car.objects.create(
                car_owner_id=car_owner.id,
                model="hatch",
                price=484845.500,
                color="gray"
            )
            car.save()

        except ValidationError:
            self.fail()

        else:
            self.assertIsInstance(car_owner, CarOwner)
            self.assertEqual(car_owner.name, 'Antonio')

            self.assertIsInstance(car, Car)
            self.assertEqual(car.model, 'hatch')
            self.assertEqual(car.price, 484845.500)
            self.assertEqual(car.color, 'gray')

    def test_with_invalid_color_choice(self):

        with self.assertRaises(ValidationError):
            car_owner = CarOwner.objects.create(
                name="Antonio"
            )
            car_owner.save()

            car = Car.objects.create(
                car_owner_id=car_owner.id,
                model="hatch",
                price=484845.500,
                color="red"
            )
            car.full_clean()

    def test_with_invalid_model_choice(self):

        with self.assertRaises(ValidationError):
            car_owner = CarOwner.objects.create(
                name="Antonio"
            )
            car_owner.save()

            car = Car.objects.create(
                car_owner_id=car_owner.id,
                model="civic",
                price=484845.500,
                color="gray"
            )
            car.full_clean()


class CarAPITesting(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username="admin",
            email="admin@testing.com",
            password="Test123")

        self.superuser.save()

        api_token_response = self.client.post("/api-token-auth", {
            'username': self.superuser.username,
            'password':  "Test123"
        })

        self.token = api_token_response.json()["token"]

        self.car_owner = CarOwner.objects.create(
            name="Antonio"
        )
        self.car_owner.save()

        Car.objects.create(
            car_owner_id=self.car_owner.id,
            model="hatch",
            price=484845.500,
            color="gray"
        )
        Car.objects.create(
            car_owner_id=self.car_owner.id,
            model="sedan",
            price=484835.500,
            color="yellow"
        )

    def test_car_listing(self):
        authorization_header = {"HTTP_AUTHORIZATION": f"Token {self.token}"}

        http_response = self.client.get(
            "/car_owner/" + str(self.car_owner.id) + "/cars", **authorization_header, format="json")

        http_response_data = http_response.json()

        self.assertEqual(len(http_response_data), 2)
        self.assertEqual(http_response_data[0]["model"], 'hatch')
        self.assertEqual(http_response_data[0]["price"], 484845.500)
        self.assertEqual(http_response_data[0]["color"], 'gray')
        self.assertEqual(
            http_response_data[0]["car_owner_id"], self.car_owner.id)

        self.assertEqual(
            http_response_data[1]["car_owner_id"], self.car_owner.id)
        self.assertEqual(http_response_data[1]["model"], 'sedan')
        self.assertEqual(http_response_data[1]["price"], 484835.500)
        self.assertEqual(http_response_data[1]["color"], 'yellow')

        self.assertEqual(http_response.status_code, 200)

    def test_car_creation(self):
        authorization_header = {"HTTP_AUTHORIZATION": f"Token {self.token}"}

        http_response = self.client.post("/car_owner/" + str(self.car_owner.id) + "/cars", {
            'model': 'hatch',
            'price': 20037,
            'color': 'gray'
        }, **authorization_header, format="json")

        http_response_data = http_response.json()

        self.assertEqual(Car.objects.count(), 3)
        self.assertEqual(http_response_data["car_owner_id"], self.car_owner.id)
        self.assertEqual(http_response_data["model"], 'hatch')
        self.assertEqual(http_response_data["price"], 20037)
        self.assertEqual(http_response_data["color"], 'gray')

        self.assertEqual(http_response.status_code, 201)

    def test_owner_cannot_have_more_than_3_cars(self):
        authorization_header = {"HTTP_AUTHORIZATION": f"Token {self.token}"}

        Car.objects.create(
            car_owner_id=self.car_owner.id,
            model="hatch",
            price=48345.500,
            color="yellow"
        )

        http_response = self.client.post("/car_owner/" + str(self.car_owner.id) + "/cars", {
            'model': 'sedan',
            'price': 20037,
            'color': 'yellow'
        }, **authorization_header, format="json")

        http_response_data = http_response.json()

        self.assertEqual(Car.objects.count(), 3)
        self.assertEqual(
            http_response_data["message"], "a person should have up to 3 cars")
        self.assertEqual(http_response.status_code, 400)

    def test_cannot_create_car_invalid_model(self):
        authorization_header = {"HTTP_AUTHORIZATION": f"Token {self.token}"}

        http_response = self.client.post("/car_owner/" + str(self.car_owner.id) + "/cars", {
            'model': 'suv',
            'price': 20037,
            'color': 'yellow'
        }, **authorization_header, format="json")

        http_response_data = http_response.json()

        self.assertEqual(
            http_response_data["model"][0], "\"suv\" is not a valid choice.")
        self.assertEqual(http_response.status_code, 400)

    def test_cannot_create_car_invalid_color(self):
        authorization_header = {"HTTP_AUTHORIZATION": f"Token {self.token}"}

        http_response = self.client.post("/car_owner/" + str(self.car_owner.id) + "/cars", {
            'model': 'sedan',
            'price': 20037,
            'color': 'red'
        }, **authorization_header, format="json")

        http_response_data = http_response.json()

        self.assertEqual(
            http_response_data["color"][0], "\"red\" is not a valid choice.")
        self.assertEqual(http_response.status_code, 400)

    def test_cannot_create_car_with_invalid_auth_header(self):
        authorization_header = {"HTTP_AUTHORIZATION": f"Token anything"}

        http_response = self.client.post("/car_owner/" + str(self.car_owner.id) + "/cars", {
            'model': 'sedan',
            'price': 20037,
            'color': 'red'
        }, **authorization_header, format="json")

        http_response_data = http_response.json()

        self.assertEqual(http_response_data["detail"], "Invalid token.")
        self.assertEqual(http_response.status_code, 401)

    def test_cannot_create_car_with_no_auth_header(self):
        http_response = self.client.post("/car_owner/" + str(self.car_owner.id) + "/cars", {
            'model': 'sedan',
            'price': 20037,
            'color': 'red'
        }, format="json")

        http_response_data = http_response.json()

        self.assertEqual(
            http_response_data["detail"], "Authentication credentials were not provided.")
        self.assertEqual(http_response.status_code, 401)


class CarOwnerAPITesting(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username="admin",
            email="admin@testing.com",
            password="Test123")

        self.superuser.save()

        api_token_response = self.client.post("/api-token-auth", {
            'username': self.superuser.username,
            'password':  "Test123"
        })

        self.token = api_token_response.json()["token"]

    def test_car_owner_listing(self):
        authorization_header = {"HTTP_AUTHORIZATION": f"Token {self.token}"}

        CarOwner.objects.create(
            name="Antonio"
        )
        CarOwner.objects.create(
            name="Padua"
        )
        self.car_owner.save()

        http_response = self.client.get("/car_owners", **authorization_header, format="json")

        http_response_data = http_response.json()

        self.assertEqual(len(http_response_data), 2)
        
        self.assertEqual(http_response_data[0]["name"], 'Antonio')
        self.assertEqual(http_response_data[0]["id"], 1)

        self.assertEqual(http_response_data[1]["name"], 'Padua')
        self.assertEqual(http_response_data[1]["id"], 2)

        self.assertEqual(http_response.status_code, 200)

    def test_car_owner_creation(self):
        authorization_header = {"HTTP_AUTHORIZATION": f"Token {self.token}"}

        http_response = self.client.post("/car_owners", {
            'name': 'Antonio',
        }, **authorization_header, format="json")

        http_response_data = http_response.json()

        
        self.assertEqual(http_response_data["name"], 'Antonio')

        self.assertEqual(http_response.status_code, 201)

    def test_cannot_create_car_with_invalid_auth_header(self):
        authorization_header = {"HTTP_AUTHORIZATION": f"Token anything"}

        http_response = self.client.post("/car_owners", {
            'name': 'Padua',
        }, **authorization_header, format="json")

        http_response_data = http_response.json()

        self.assertEqual(http_response_data["detail"], "Invalid token.")
        self.assertEqual(http_response.status_code, 401)

    def test_cannot_create_car_owner_with_no_auth_header(self):
        http_response = self.client.post("/car_owners", {
            'name': 'Junior',
        }, format="json")

        http_response_data = http_response.json()

        self.assertEqual(
            http_response_data["detail"], "Authentication credentials were not provided.")
        self.assertEqual(http_response.status_code, 401)
