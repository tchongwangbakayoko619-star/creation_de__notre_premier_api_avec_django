from api.models import Product
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from .serealiser import ProductSerializer, ProductSerializer2
from rest_framework.decorators import api_view
#comment developper une a pi avec le decorateur @api_view de DRF
@api_view(['GET', 'POST','PUT','DELETE', 'PATCH'])
def product_api_view(request,pk=None, *args, **kwargs):
    if request.method == 'GET':
        if pk is not None:
            try:
                product = get_object_or_404(Product,pk=pk)
                serializer = ProductSerializer(product)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            product = serializer.save()  # Cela appelle create()
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        if pk is None:
            return Response({'error': 'Product ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            updated_product = serializer.save()
            return Response(ProductSerializer(updated_product).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        if pk is None:
            return Response({'error': 'Product ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PATCH':
        if pk is None:
            return Response({'error': 'Product ID is required for partial update'}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            updated_product = serializer.save()
            return Response(ProductSerializer(updated_product).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
