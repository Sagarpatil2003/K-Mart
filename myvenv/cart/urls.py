from django.urls import path
from . import views


urlpatterns = [
    path('add-to-cart', views.add_to_cart_view, name="add_to_cart_view"),
    path('my_cart', views.my_cart_view, name="my_cart_view"),
    path('delete_cart_item/<int:cart_id>', views.delete_cart_item_view, name="delete_cart_item_view"),
    path('checkout', views.checkout, name="checkout"),
    path('thank_you', views.thank_you_view, name='thank_you_view')
]