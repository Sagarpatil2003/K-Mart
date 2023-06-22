from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import viewsets, views, response, filters, authentication, status
from rest_framework.permissions import IsAuthenticated
from django.db.models import F, Sum, Prefetch
from django.contrib.auth.models import User
from product.models import product_category, Product
from cart.models import Cart
from .serializers import UserSerializer, ProductCategorySerializer, ProductSerializer, CartSerializer


class UserAuthView(ObtainAuthToken):
    """User Authentication API"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserView(viewsets.ModelViewSet):
    """User CRUD Operation"""
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_superuser=False, is_staff=False)


class ProductCategoryView(views.APIView):
    serializer_class = ProductCategorySerializer

    def get(self, request):
        product_categories = product_categories.objects.filter(status=True)
        serializer = self.serializer_class(product_categories, many=True)
        return response.Response(serializer.data)


class ProductCategoryViewSets(viewsets.ModelViewSet):
    """Product Category API"""
    serializer_class = ProductCategorySerializer
    queryset = product_category.objects.filter(status=True)
    http_method_names = ['get']


class ProductViewSets(viewsets.ModelViewSet):
    """Product API"""
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(status=True).prefetch_related('product_category')
    http_method_names = ['get']
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['product_category__slug']
    ordering_fields = ['price']


class AdditionalInfoCartView(views.APIView):
    # Additional info about the current user's cart
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        shipping = 50
        discount = 0
        cart_products = Cart.objects.filter(user=request.user).annotate(sub_total=F('product__price') * F('quantity'))
        sub_total = cart_products.aggregate(total=Sum('sub_total'))['total']
        grand_total = sub_total + shipping
        return response.Response({'shipping': shipping, 'discount': discount, 'sub_total': sub_total, 'grand_total': grand_total})


class CartView(views.APIView):
    """Cart API View"""
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get(self, request, cartId=None):
        """List all cart items for the current user"""
        cart_products = Cart.objects.filter(user=request.user).annotate(
            sub_total=F('product__price') * F('quantity')
        ).select_related('product').prefetch_related('product__product_category')
        serializer = self.serializer_class(cart_products, many=True)
        return response.Response(serializer.data)

    def post(self, request, cartId=None):
        """Add to cart"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            quantity = serializer.validated_data.get('quantity')
            product = serializer.validated_data.get('product')
            variation = serializer.validated_data.get('variation')
            cart, is_created = Cart.objects.get_or_create(user=request.user, product=product, variation=variation)
            cart.quantity = quantity
            cart.save()
            return response.Response({'status': 'Success'}, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cartId=None):
        try:
            Cart.objects.get(id=cartId).delete()
            return response.Response({'status': 'success'})
        except Cart.DoesNotExist:
            return response.Response({'details': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
