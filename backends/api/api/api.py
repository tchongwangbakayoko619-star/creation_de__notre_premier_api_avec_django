from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from api.models import Product
from api.api.serealiser import ProductSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def product_api_view(request, pk=None, *args, **kwargs):
    if request.method == 'GET':
        if pk is not None:
            product = get_object_or_404(Product, pk=pk)
            serializer = ProductSerializer(product, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            product = serializer.save()
            return Response(ProductSerializer(product, context={'request': request}).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        if pk is None:
            return Response({'error': 'Product ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            updated_product = serializer.save()
            return Response(ProductSerializer(updated_product, context={'request': request}).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        if pk is None:
            return Response({'error': 'Product ID is required for partial update'}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            updated_product = serializer.save()
            return Response(ProductSerializer(updated_product, context={'request': request}).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is None:
            return Response({'error': 'Product ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
