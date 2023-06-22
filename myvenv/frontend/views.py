from django.shortcuts import render
from central.models import Slider
from product.models import product_category, Product, ProductTag
from central.models import WebsiteSetting
from django.views import View


def home_page(request):
    """ Home page of k-mart E-com  """
    """ selected_related """
    sliders = Slider.objects.filter(status=True)
    product_categories = product_category.objects.filter(status=True, show_on_homepage=True)
    fashion_products_one = Product.objects.select_related('product_category').filter(status=True)[0:2]
    fashion_products_two = Product.objects.select_related('product_category').filter(status=True)[2:4]
    product_tags = ProductTag.objects.filter(status=True)[0:2]
    context = {
        'sliders' : sliders,
        'product_categories' : product_categories,
        'fashion_products_one' : fashion_products_one,
        'fashion_products_two' : fashion_products_two,
        'product_tags' : product_tags
    }
    return render(request, 'home.html', context)

""" Products with category id """

# def product_listing(request, category_id):
#     navigation_categories = ProductCategory.objects.filter(status=True)
#     website_setting = WebsiteSetting.objects.all().last()
#     # products = Product.objects.filter(status=True, product_category=category_id)
#     products = Product.objects.filter(status=True, product_category_id=category_id) # recomended
#     print(products)
#     context = {
#         'navigation_categories' : navigation_categories,
#         'website_setting' : website_setting,
#         'products' : products
#     }
#     return render(request, 'product/product_listing.html', context)

def product_listing(request, product_category_slug=None):
    """ Products with category slug """
    filters = {
        'status':True
    }
    if request.GET.get('search'):
        filters['name__icontains'] = request.GET.get('search')

    if product_category_slug:
        filters['product_category__slug'] = product_category_slug
    products = Product.objects.filter(**filters) # recomended
    context = {
        'products' : products
    }
    return render(request, 'product/product_listing.html', context)


class ProductDetails(View):

    def get(self, request, product_slug):
        try:
            product = Product.objects.select_related('product_category').prefetch_related('ProductImage').get(slug=product_slug)
            similar_products = Product.objects.filter(status=True, product_category=product.product_category).exclude(id=product.id)
            context = {
                'product' : product,
                'similar_products' : similar_products,
            }
            return render(request, 'product/product_details.html', context)
        except Product.DoesNotExist:
            pass



