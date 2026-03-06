from api.models import Product
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework import status
from rest_framework.response import Response
from api.api.serealiser import ProductSerializer,ProductSerializer2
from rest_framework.decorators import action
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer2
        return ProductSerializer   
    @action(detail=False, methods=['get'], url_path='expensive', url_name='expensive')
    def expensive(self,request,*args,**kwargs):
        products=Product.objects.filter(price__gt=9)
        context ={'request': request}
        serializer=ProductSerializer(products,many=True,context=context)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def get_queryset(self):
        return super().get_queryset().filter(price__gt=10)


