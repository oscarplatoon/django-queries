from .models import Product
from django.db.models import Q, Avg, Max
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
        return Product.objects.filter(rating=rating)

    @classmethod
    def by_rating_range(cls, start, end):
        return Product.objects.filter(rating__range=(start, end))

    @classmethod
    def by_rating_and_color(cls, rating, color):
        rating_matches = Product.objects.filter(rating=rating)
        color_matches = Product.objects.filter(color=color)
        return rating_matches.intersection(color_matches)

    @classmethod
    def by_rating_or_color(cls, rating, color):
        rating_matches = Product.objects.filter(rating=rating)
        color_matches = Product.objects.filter(color=color)
        return rating_matches.union(color_matches)

    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color=None).count()

    @classmethod
    def below_price_or_above_rating(cls, price_cents, rating):
        # using .union()
        # below_price_set = Product.objects.filter(
        #     price_cents__lt=price_cents)
        # above_rating_set = Product.objects.filter(rating__gt=rating)
        # return (below_price_set.union(above_rating_set)).order_by('id')

        # using Q objects
        return Product.objects.filter(Q(price_cents__lt=price_cents) | Q(rating__gt=rating))

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.order_by('category', '-price_cents')

    @classmethod
    def products_by_manufacturer_with_name_like(cls, manufacturer_name):
        return Product.objects.filter(manufacturer__contains=manufacturer_name)

    @classmethod
    def manufacturer_names_for_query(cls, manufacturer_name):
        # flat=True returns single values, not tuples
        return Product.objects.filter(manufacturer__contains=manufacturer_name).values_list('manufacturer', flat=True)

    @classmethod
    def not_in_a_category(cls, category):
        return Product.objects.exclude(category=category)

    @classmethod
    def limited_not_in_a_category(cls, category, limit):
        return Product.objects.exclude(category=category)[0:limit]

    @classmethod
    def category_manufacturers(cls, category):
        return Product.objects.filter(category=category).values_list('manufacturer', flat=True)

    @classmethod
    def average_category_rating(cls, category):
        return Product.objects.filter(category=category).aggregate(Avg('rating'))

    @classmethod
    def greatest_price(cls):
        return Product.objects.aggregate(Max('price_cents'))

    @classmethod
    def longest_model_name(cls):
        # orders objects by the length of model, descending (hence the '-')
        # gets the longest model name queryset and returns the id of that
        return Product.objects.order_by(-Length('model'))[0].id

    @classmethod
    def ordered_by_model_length(cls):
        return Product.objects.order_by(Length('model'))
