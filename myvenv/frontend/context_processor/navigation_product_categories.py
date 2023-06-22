from product.models import product_category

def navigation_product_categories(request):
    """For Navigation Product Dropdown """
    navigation_product_categories=product_category.objects.filter(status=True)
    return{'navigation_product_categories':navigation_product_categories}