from django.contrib import admin
from .models import Lista, Item, Site, TipoWishlist

admin.site.register(Lista)
admin.site.register(Item)
admin.site.register(Site)
admin.site.register(TipoWishlist)