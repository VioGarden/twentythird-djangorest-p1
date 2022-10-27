# simplify - where all django api urls are (can be done in root urls.py too)

from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', views.api_home) # localhost:8000/api/
    # path('products/', include('products.urls')) <-- could do

]


