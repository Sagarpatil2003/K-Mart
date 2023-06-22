from central.models import WebsiteSetting
from cart.models  import Cart
from django.db.models import Sum

def website_setting(request):
    """Web Site Setting Display dynamic ,LOGO ,TITLE ,And Address on frontend """
    website_setting=  WebsiteSetting.objects.all().last()
    return{'global_website_setting':website_setting}


 
# def cart_count(request):
#    # Display  cart count
#     quantity = 0
#     if request.user.is_authenticated:
#         carts= Cart.objects.filter(data=request.user)
#         for cart in carts:
#             quantity=quantity + cart.quantity

#         return quantity


def cart_count(request):
    if request.user.is_authenticated:
        quantity = Cart.objects.filter(data=request.user).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        return quantity
    return 0


