from os import name
from django.db.models.aggregates import Max
from .models import Product 
from django.db.models import Avg
from django.db.models.functions import Length

class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()
    
    @classmethod
    def find_by_model(cls, string):
        return Product.objects.get(model=string)

    @classmethod
    def last_record(cls):
        return Product.objects.last()

    @classmethod
    def by_rating(cls, input):
        return Product.objects.filter(rating=input)

    @classmethod
    def by_rating_range(cls, x,y):
        return Product.objects.filter(rating__gte=x) & Product.objects.filter(rating__lte=y)

    @classmethod
    def by_rating_and_color(cls,r,c):
        return Product.objects.filter(rating=r) & Product.objects.filter(color=c) 

    @classmethod
    def by_rating_or_color(cls, r, c):
        return Product.objects.filter(rating=r) | Product.objects.filter(color=c) 

    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color__isnull=True).count()

    @classmethod
    def below_price_or_above_rating(cls,p,r):
        return Product.objects.filter(price_cents__lt=p) | Product.objects.filter(rating__gt=r)

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.order_by('category','-price_cents')
    
    @classmethod
    def products_by_manufacturer_with_name_like(cls,string):
        return Product.objects.filter(manufacturer__contains=string)

    @classmethod
    def manufacturer_names_for_query(cls,string):
        return Product.objects.values_list('manufacturer',flat=True).filter(manufacturer__contains=string)
    
    @classmethod
    def not_in_a_category(cls,c):
        return Product.objects.exclude(category=c)
    
    @classmethod
    def limited_not_in_a_category(cls,c,n):
        return Product.objects.exclude(category=c)[:n]

    @classmethod
    def category_manufacturers(cls,c):
        return Product.objects.values_list('manufacturer',flat=True).filter(category=c)
    
    @classmethod
    def average_category_rating(cls,c):
        return Product.objects.filter(category=c).aggregate(Avg('rating'))

    @classmethod
    def greatest_price(cls):
        return Product.objects.aggregate(Max('price_cents'))

    @classmethod
    def longest_model_name(cls):
        return Product.objects.values_list('id',flat=True).order_by(Length('model').desc())[:1].get()
    
    @classmethod
    def ordered_by_model_length(cls):
        return Product.objects.values_list('id',flat=True).order_by(Length('model').asc())