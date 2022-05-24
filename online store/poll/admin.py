from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'ct_category_name')
    list_display_links = ('id', 'ct_category_name')
    search_fields = ('ct_category_name',)
    prepopulated_fields = {"slug": ("ct_category_name",)}

class ProductAdmin(admin.ModelAdmin):
   
    prepopulated_fields = {"slug": ("p_title",)}



admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')