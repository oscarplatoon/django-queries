from .models import Product 

class ProductCrud:

    @classmethod
    def get_all_products(cls):
        return Product.objects.all()

    @classmethod
    def find_by_model(cls, model):
        return Product.objects.get(model=model)
    
    @classmethod
    def last_record(cls):
        return Product.objects.last()

    @classmethod
    def by_rating(cls,rating):
        return Product.objects.filter(rating=rating)
    
    @classmethod
    def by_rating_range(cls, start_rating, stop_rating):
        return Product.objects.filter(rating__range=(start_rating, stop_rating))
    
    @classmethod
    def by_rating_and_color(cls, rating, color):
        return Product.objects.filter(rating=rating, color=color)
    
    @classmethod
    def by_rating_or_color(cls, rating, color):
        rating_match = Product.objects.filter(rating=rating)
        color_match = Product.objects.filter(color=color)
        return color_match.union(rating_match)
    
    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color=None).count()
    
    @classmethod
    def below_price_or_above_rating(cls, price_cents, rating):
       return Product.objects.filter(Q(price_cents__lt=price_cents) | Q(rating__gt=rating))
   
   


    




        