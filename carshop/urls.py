from django.urls import path

from . import views

urlpatterns = [
    path('car_owners', views.CarOwnerView.as_view()),
    path('car_owner/<int:owner_id>/cars', views.CarView.as_view()),
]
