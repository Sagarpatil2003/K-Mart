from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name="home_page"),
    # path('product-listing/<category_id>', views.product_listing, name="product_listing"),
    path('product-listing/', views.product_listing, name="product_listing"),
    path('product-listing/<slug:product_category_slug>', views.product_listing, name="product_listing"),
    path('product-details/<slug:product_slug>', views.ProductDetails.as_view(), name="ProductDetails")
]