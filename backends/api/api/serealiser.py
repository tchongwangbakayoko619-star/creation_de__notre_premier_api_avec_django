from rest_framework import serializers
from api.models import Product

class ProductSerializer(serializers.ModelSerializer):
    Email = serializers.EmailField(write_only=True, required=False)
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    price_in_fcfa = serializers.SerializerMethodField(read_only=True)
    description_summary = serializers.SerializerMethodField(read_only=True)
    link = serializers.HyperlinkedIdentityField(view_name='product_api_view_detail', lookup_field='pk')
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'Email', 'price', 'price_in_fcfa', 'description_summary', 'link']
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
        return super().create(validated_data)


class ProductSerializer2(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)
    price_in_fcfa = serializers.SerializerMethodField()

    def get_price_in_fcfa(self, obj):
        return f"{obj.price} FCFA"

       

