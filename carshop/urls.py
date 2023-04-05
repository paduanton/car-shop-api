from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token 
from . import views

urlpatterns = [
    path('car_owners', views.CarOwnerView.as_view()),
    path('car_owner/<int:owner_id>/cars', views.CarView.as_view()),
    path('api-token-auth', obtain_auth_token, name='api_token_auth'),
]
