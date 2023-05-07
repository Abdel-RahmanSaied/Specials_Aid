from django.contrib import admin
from . models import *
# Register your models here.


class symbol_collection(admin.ModelAdmin):
    list_display = ("name", "size", "dimension_of_symbols", "collection_image")
    list_display_links = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)


class symbols(admin.ModelAdmin):
    list_display = ("name", "image", "collection_name")
    list_display_links = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)


admin.site.register(Symbols_Collectoin, )
admin.site.register(symbol, )
