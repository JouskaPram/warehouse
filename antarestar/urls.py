
from django.contrib import admin
from django.urls import path
from antarestardata.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminpage',adminpage),
    path('tambahpo/',addpreorder),
    path('',base),
    path('preorder',getpo)
]
