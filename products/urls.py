from django.urls import path

from products.views import products, bucket_add, bucket_remove

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:category_id>/', products, name='category'),
    path('buckets/add/<int:product_id>/', bucket_add, name='bucket_add'),
    path('page/<int:page_number>', products, name='paginator'),
    path('buckets/remove/<int:bucket_id>/', bucket_remove, name='bucket_remove'),

]
