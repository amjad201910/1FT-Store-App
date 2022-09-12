from django.urls import include, path
from rest_framework import routers
from Product import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Product.urls')),
]