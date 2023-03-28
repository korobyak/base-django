from django.contrib import admin

from src.users.models import User
from src.products.admin import BucketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BucketAdmin,)
    extra = 0