from django.urls import path
from .views import AutoList, EditAutoView, CreateSale

urlpatterns = [
    path('', AutoList.as_view(), name="list"),
    path('sale/new/', CreateSale.as_view(), name="create"),
    path('sale/<int:pk>/', EditAutoView.as_view(), name="edit"),
]
