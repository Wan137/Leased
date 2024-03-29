from django.urls import path
from .views import PropertyList, PropertyDetail

urlpatterns = [
    path('flat/', PropertyList.as_view(), name='property-list'),
    path('flat/<int:pk>/', PropertyDetail.as_view(), name='property-detail'),
]