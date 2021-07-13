from django.contrib import admin
from django.contrib.admin import ModelAdmin

from posts.models import Post, Product


@admin.register(Post)
class PostAdmin(ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    pass
