from .models import Product 
from django.db.models import Avg, Max
from django.db.models.functions import Length



class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()

    @classmethod
    def find_by_model(cls, model_name):
        return Product.objects.get(model=model_name)

    @classmethod
    def last_record(cls):
        return Product.objects.last()

    @classmethod
    def by_rating(cls, rating):
        return Product.objects.filter(rating__exact = 3.5)

    @classmethod
    def by_rating_range(cls, lower_bound, upper_bound):
        return Product.objects.filter(rating__range=(lower_bound, upper_bound))

    @classmethod
    def by_rating_and_color(cls, input_rating, input_color):
        return Product.objects.filter(rating = input_rating, color = input_color )

    @classmethod
    def by_rating_or_color(cls, input_rating, input_color): 
        return Product.objects.filter(rating = input_rating) | Product.objects.filter(color = input_color)

    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color__isnull = True).count()

    @classmethod
    def below_price_or_above_rating(cls, below_price, above_rating):
        return Product.objects.filter(price_cents__lt=below_price) | Product.objects.filter(rating__gt=above_rating)

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.all().order_by('category', '-price_cents')

    @classmethod
    def products_by_manufacturer_with_name_like(cls, manufacturer):
        return Product.objects.filter(manufacturer__contains=manufacturer)
    
    @classmethod
    def manufacturer_names_for_query(cls, manufacturer):
        product_list = list(Product.objects.filter(manufacturer__contains=manufacturer))
        output_list = []
        for elem in product_list:
          output_list.append(elem.manufacturer)
        return output_list

    @classmethod
    def not_in_a_category(cls, category):
        return Product.objects.exclude(category__contains = category)

    @classmethod
    def limited_not_in_a_category(cls, category, limit):
        return Product.objects.exclude(category__contains = category)[:limit]
    
    @classmethod
    def category_manufacturers(cls, category):
        product_list = list(Product.objects.filter(category__contains=category))
        output_list = []
        for elem in product_list:
          output_list.append(elem.manufacturer)
        return output_list

    @classmethod
    def average_category_rating(cls, category_name):
        return Product.objects.filter(category__contains=category_name).aggregate(Avg('rating'))

    @classmethod
    def greatest_price(cls):
        return Product.objects.all().aggregate(Max('price_cents'))

    @classmethod
    def longest_model_name(cls):
        product_object = Product.objects.order_by(Length('model').desc())[:1]
        for elem in product_object:
            return elem.id
    
    @classmethod
    def ordered_by_model_length(cls):
        return Product.objects.order_by(Length('model').asc())