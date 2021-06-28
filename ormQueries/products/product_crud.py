from .models import Product 
from django.db.models import Q, Avg, Max
from django.db.models.functions import Length
class ProductCrud():
    
    @classmethod
    def get_all_products(cls):

        return(Product.objects.all())
    
    @classmethod
    def find_by_model(cls, model_name):
        for product in Product.objects.all():
            if product.model == model_name:
                return product
        return("Model not found.")
    
    @classmethod
    def last_record(cls):
        return(Product.objects.last())

    @classmethod
    def by_rating(cls, search_for_rating):
        return Product.objects.filter(rating__exact = search_for_rating)

    @classmethod
    def by_rating_range(cls, low_end, high_end):
        return Product.objects.filter(rating__range=(low_end, high_end))

    @classmethod
    def by_rating_and_color(cls, rating, color):
        return Product.objects.filter(rating__exact = rating, color__exact=color)

    @classmethod
    def by_rating_or_color(cls, search_rating, search_color):
        return(Product.objects.filter(rating__exact=search_rating) | Product.objects.filter(color__exact=search_color))

    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color__exact=None).count()

    @classmethod
    def below_price_or_above_rating(cls, target_price, target_rating):
        return(Product.objects.filter(price_cents__lt=target_price) | Product.objects.filter(rating__gt=target_rating))

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_descending(self):
        return(Product.objects.all().order_by('category', '-price_cents'))

    @classmethod
    def products_by_manufacturer_with_name_like(cls, search_string):
        return(Product.objects.filter(manufacturer__icontains=search_string))

    @classmethod
    def manufacturer_names_for_query(cls, search_group):
        manufacturers = Product.objects.filter(manufacturer__icontains=search_group).order_by().values_list('manufacturer', flat=True).distinct('manufacturer')
        return(manufacturers)

    @classmethod
    def not_in_a_category(cls, search_category):
        return(Product.objects.filter(~Q(category__icontains=search_category)))

    @classmethod
    def limited_not_in_a_category(cls, search_category, limit):
        return(Product.objects.filter(~Q(category__icontains=search_category)))[:limit]

    @classmethod
    def category_manufacturers(cls, category_filter):
        return(Product.objects.filter(category__exact=category_filter).values_list('manufacturer', flat=True))

    @classmethod
    def average_category_rating(cls, category_filter):
        return(Product.objects.filter(category__exact=category_filter).aggregate(Avg('rating')))

    @classmethod
    def greatest_price(cls):
        return(Product.objects.aggregate(Max('price_cents')))

    #The pre-Length way of solving this.
    @classmethod
    def longest_model_name(cls):
        return(len(Product.objects.aggregate(Max('model'))['model__max']))

    # The way slicker way of solving this with Length
    @classmethod
    def ordered_by_model_length(cls):
        return(Product.objects.order_by(Length('model')))