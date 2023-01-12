from django.contrib import admin
from antarestardata.models import *

# Register your models here.
class PreorderAdmin(admin.ModelAdmin):
    list_display=['produk','nama_penulis']

admin.site.register(Preorder)
admin.site.register(Suplier)
admin.site.register(AppPreorder)

