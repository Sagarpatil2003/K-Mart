from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('product_categories', views.ProductCategoryViewSets)
router.register('products', views.ProductViewSets)


urlpatterns = [
    path('', include(router.urls)),
    path('product_categories_apiview', views.ProductCategoryView.as_view()),
    path('login/', views.UserAuthView.as_view()),
    path('carts/', views.CartView.as_view()),
    path('carts/<cartId>/', views.CartView.as_view()),
    path('carts-info/', views.AdditionalInfoCartView.as_view()),
]