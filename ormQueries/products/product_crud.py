from .models import Product


class ProductCrud:

    @classmethod
    def get_all_products(cls):
        return Product.objects.all()

    @classmethod
    def find_by_model(cls, id):
        for item in Product.objects.all():
            if item.model == id:
                return item

    @classmethod
    def last_record(cls):
        return Product.objects.last()

    @classmethod
    def by_rating(cls, rate_num):
        return Product.objects.filter(rating__exact=rate_num)

    @classmethod
    def by_rating_range(cls, num1, num2):
        return Product.objects.filter(rating__range=(num1, num2))

    @classmethod
    def by_rating_and_color(cls, rating, color):
        return Product.objects.filter(rating=rating, color=color)

    @classmethod
    def rating_or_color(self, rating, color):
        return Product.objects.filter(rating == rating, color == color)
