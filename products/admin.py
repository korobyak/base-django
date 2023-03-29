from django.contrib import admin

from products.models import ProductCategory, Product, Bucket

admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category', )
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

class BucketAdmin(admin.TabularInline):
    model = Bucket
    fields = ('product', 'quantity',)