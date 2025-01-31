from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import ProductSerializer

# Pagination class for GET requests
class ProductPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductList(APIView):
    # Set default permission for GET requests as AllowAny (anonymous users can read)
    permission_classes = [AllowAny]
    pagination_class = ProductPagination

    def get(self, request):
        # Filter logic for GET requests
        name_filter = request.query_params.get('name', None)
        price_min = request.query_params.get('price_min', None)
        price_max = request.query_params.get('price_max', None)

        products = Product.objects.all()

        if name_filter:
            products = products.filter(name__icontains=name_filter)
        if price_min:
            products = products.filter(price__gte=price_min)
        if price_max:
            products = products.filter(price__lte=price_max)

        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        # Ensure the user is authenticated for POST requests
        self.permission_classes = [IsAuthenticated]  # Override for POST
        # Recheck permissions before continuing
        self.check_permissions(request)

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            # Currency conversion logic: IDR to SGD (1 SGD = 10,000 IDR)
            if 'price_idr' in request.data:
                price_idr = float(request.data['price_idr'])
                price_sgd = price_idr / 10000
                serializer.validated_data['price'] = price_sgd
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            if 'price_idr' in request.data:
                price_idr = float(request.data['price_idr'])
                price_sgd = price_idr / 10000
                serializer.validated_data['price'] = price_sgd
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def product_list(request):
    return render(request, 'product_list.html')
def login_view(request):
    return render(request, 'login.html') 
