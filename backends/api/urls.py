from django.urls import path,include
from . import views
from api.api.api import product_api_view
from api.api.mixins import ProductListCreateAPIView,  ProductDetailAPIView, ProductCreateAPIView, ProductUpdateAPIView,ProductDeleteAPIView, CombineAPViewlet
from rest_framework.authtoken.views import obtain_auth_token
name='api'
urlpatterns = [
    path('auth/', obtain_auth_token, name='api_token_auth'),
    path('', views.home, name='home'),
    path('product/', product_api_view, name='product_api_view'),
    path('product/<int:pk>/', product_api_view, name='product_api_view_detail'),
    path('', include('api.api.routers')),
    path('v2/product-list/', ProductListCreateAPIView.as_view(), name='product_list_create_api_view'),
    path('v2/product-detail/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail_api_view'),
    path('v2/product-create/', ProductCreateAPIView.as_view(), name='product_create_api_view'),
    path('v2/product-update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update_api_view'),
    path('v2/product-delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product_delete_api_view'),
    path('v2/product-combine/', CombineAPViewlet.as_view(), name='product_combine_api_view'),
    path('v2/product-combine/<int:pk>/', CombineAPViewlet.as_view(), name='product_combine_api_view_detail'),
]
