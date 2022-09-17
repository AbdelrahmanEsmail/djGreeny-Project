from rest_framework.response import Response 
from .serializers import ProductSerializer , CategorySerializer , BrandSerializer , CategoryDetailSerializer , BrandDetailSerializer
from .models import Category, Product , Brand
from rest_framework.decorators import api_view
# import django_filters.rest_framework


# @api_view(['GET'])
# def product_list_api(request):
#     products = Product.objects.all()[:10]
#     data = ProductSerializer(products,many=True).data
#     return Response({'Success':True, 'Product List': data})



# @api_view(['GET'])
# def product_detail(request,id):
#     product = Product.objects.get(id=id)
#     data = ProductSerializer(product).data
#     return Response({'Success':True , 'Product': data})



from rest_framework import generics 
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

class ProductListAPI(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all() 
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAuthenticated]
    # 
    
    
class ProductDetailAPI(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all() 
    permission_classes = [IsAuthenticated]
    
    
# category list  , detail 
class CategoryListAPI(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all() 
    permission_classes = [IsAuthenticated]



class CategoryDetailAPI(generics.RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all() 
    permission_classes = [IsAuthenticated]

# brand list , brand detail 
class BrandListAPI(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all() 
    permission_classes = [IsAuthenticated]



class BrandDetailAPI(generics.RetrieveAPIView):
    serializer_class = BrandDetailSerializer
    queryset = Brand.objects.all() 
    permission_classes = [IsAuthenticated]
    
    
    
    
### Viewsets 
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all() 