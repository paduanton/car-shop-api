from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Car, CarOwner


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
