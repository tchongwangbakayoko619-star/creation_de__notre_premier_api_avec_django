from api.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    Email = serializers.EmailField(write_only=True, required=False)  # Champ pour recevoir l'email dans la requête POST
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'update_at')
    def create(self, validated_data):
        self.Email = validated_data.pop('Email', None)  # Extraire l'email si présent
        print(f"Email reçu dans le serializer: {self.Email}")  # Afficher l'email pour vérification
        return super().create(validated_data) 
       
class ProductSerializer2(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)
