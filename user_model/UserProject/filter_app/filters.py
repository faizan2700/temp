import django_filters
from filter_app.models import Product, Manufacturer

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact') 

    class Meta:
        model = Product 
        fields = {
            'price' : ['lt', 'gt'],
            'release_date' : ['exact', 'year__gt'],
        }

        