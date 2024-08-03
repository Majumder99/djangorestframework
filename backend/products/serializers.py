from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'get_discount'
        ]
        
    def get_my_discount(self, obj):
        # i can manupulate my data here too
        return obj.get_discount()