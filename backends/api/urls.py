from django.urls import path,include
from . import views
from api.api.api import product_api_view
urlpatterns = [
    path('', views.home, name='home'),
    path('product/', product_api_view, name='product_api_view'),
    path('product/<int:pk>/', product_api_view, name='product_api_view_detail'),
]
