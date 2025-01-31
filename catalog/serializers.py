from rest_framework import serializers
from catalog.models import Product

class ProductSerializer(serializers.ModelSerializer):
    price_idr = serializers.DecimalField(
        max_digits=10, decimal_places=2, write_only=True, required=True
    )
    price = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )  # 🔹 Make price read-only

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'price_idr', 'created_at', 'updated_at']

    def create(self, validated_data):
        idr_price = validated_data.pop('price_idr', None)
        if idr_price is not None:
            validated_data['price'] = idr_price / 10000  # Convert IDR to SGD
        return super().create(validated_data)

    def update(self, instance, validated_data):
        idr_price = validated_data.pop('price_idr', None)
        if idr_price is not None:
            validated_data['price'] = idr_price / 10000
        return super().update(instance, validated_data)
