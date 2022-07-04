from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token

urlpatterns = [
    # Your URLs...
    path('token/', obtain_jwt_token,name="api-jwt-auth"),
    path('token/refresh/', refresh_jwt_token),
]
