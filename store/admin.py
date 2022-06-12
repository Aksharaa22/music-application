from django.contrib import admin
from .models import movies2, Address, Category, Product, Cart, Order,History,MsProduct,MsProducttwo,MsCart,Mus,Book,Audio_store

# Register your models here.

admin.site.register(History)

admin.site.register(movies2)
admin.site.register(Mus)
admin.site.register(Book)
admin.site.register(Audio_store)

class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'locality', 'city', 'state')
    list_filter = ('city', 'state')
    list_per_page = 10
    search_fields = ('locality', 'city', 'state')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category_image', 'is_active', 'is_featured', 'updated_at')
    list_editable = ('slug', 'is_active', 'is_featured')
    list_filter = ('is_active', 'is_featured')
    list_per_page = 10
    search_fields = ('title', 'description')
    prepopulated_fields = {"slug": ("title", )}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'product_image', 'is_active', 'is_featured', 'updated_at')
    list_editable = ('slug', 'category', 'is_active', 'is_featured')
    list_filter = ('category', 'is_active', 'is_featured')
    list_per_page = 10
    search_fields = ('title', 'category', 'short_description')
    prepopulated_fields = {"slug": ("title", )}

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at')
    list_editable = ('quantity',)
    list_filter = ('created_at',)
    list_per_page = 20
    search_fields = ('user', 'product')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'status', 'ordered_date')
    list_editable = ('quantity', 'status')
    list_filter = ('status', 'ordered_date')
    list_per_page = 20
    search_fields = ('user', 'product')






class MsProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'product_image','date', 'is_active', 'is_featured', 'updated_at')
    list_editable = ('slug', 'is_active', 'is_featured')
    list_filter = ( 'is_active', 'is_featured')
    list_per_page = 10
    search_fields = ('title',  'short_description')
    prepopulated_fields = {"slug": ("title", )}


class MsProducttwoAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'product_image','date','is_active', 'is_featured', 'updated_at')
    list_editable = ('slug', 'is_active', 'is_featured')
    list_filter = ( 'is_active', 'is_featured')
    list_per_page = 10
    search_fields = ('title',  'short_description')
    prepopulated_fields = {"slug": ("title", )}


class MsCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at')
    list_editable = ('quantity',)
    list_filter = ('created_at',)
    list_per_page = 20
    search_fields = ('user', 'product')







admin.site.register(Address, AddressAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)

admin.site.register(MsProduct, MsProductAdmin)
admin.site.register(MsProducttwo, MsProducttwoAdmin)

admin.site.register(MsCart, MsCartAdmin)