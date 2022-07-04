from django.urls import path
from . import views
  
urlpatterns = [
   
    path('list/', views.view_location, name='location_list'),
    path('location_detail/<int:id>', views.location_detail),
  
]