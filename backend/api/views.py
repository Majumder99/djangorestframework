from operator import is_
from django.http import JsonResponse
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("id").first()
    data = {}
    if model_data:
        # data = model_to_dict(model_data)
        # model_data holo db theke asha data. ekhn oitake productserializer er maddhome json e convert korbo. and productserializer
        # er mddhe ami bole dicchi kon kon field amr drkr and kon model e oigulan ache. 
        #         from rest_framework import serializers
        # from .models import Product

        # class ProductSerializer(serializers.ModelSerializer):
        #     class Meta:
        #         model = Product
        #         fields = [
        #             'title',
        #             'content',
        #             'price',
        #             'sale_price',
        #             'get_discount'
        #         ]
        data = ProductSerializer(model_data).data
    return Response(data)

@api_view(['POST'])
def api_view(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        data = serializer.data
        return Response(data)
    