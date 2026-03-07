from rest_framework import serializers
from api.models import Product
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    Email = serializers.EmailField(write_only=True, required=False)
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    price_in_fcfa = serializers.SerializerMethodField(read_only=True)
    description_summary = serializers.SerializerMethodField(read_only=True)
    link = serializers.HyperlinkedIdentityField(view_name='product_api_view_detail', lookup_field='pk')
    author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'Email', 'price', 'price_in_fcfa', 'description_summary', 'link','author']
        extra_kwargs = {
            'price': {'required': True}
        }

    def get_price_in_fcfa(self, obj):
        return obj.get_price_in_fcfa()
    
    def get_description_summary(self, obj):
        return obj.get_description()
    
    def validate_name(self, value):
        if value.lower() in ['bakayoko', 'mamadou']:
            raise serializers.ValidationError("Invalid product name")
        return value
    
    def create(self, validated_data):
        email = validated_data.pop('Email', None)
        if email:
            print(f"Email reçu dans le serializer: {email}")
        # Assigner automatiquement l'utilisateur connecté comme auteur
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class ProductSerializer2(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)
    price_in_fcfa = serializers.SerializerMethodField()
    author = serializers.StringRelatedField(read_only=True)
    link = serializers.HyperlinkedIdentityField(view_name='product_api_view_detail', lookup_field='pk')

    def get_price_in_fcfa(self, obj):
        return f"{obj.price} FCFA"


class UserProductsSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'products']
    
    def get_products(self, obj):
        products = Product.objects.filter(author=obj)
        context = {'request': self.context.get('request')}
        return ProductSerializer2(products, many=True, context=context).data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
