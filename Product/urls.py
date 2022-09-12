
from django.urls import include, path
from rest_framework import routers
from Product import views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('show/', views.dessertlist.as_view(),name="show"),
    path('create/', views.dessercreate.as_view(),name="create"),
    path('add/', views.potoadd.as_view(),name="add-new"),
    path('update/<int:pk>/', views.productupdate.as_view(),name="update-detail"),
    path('showd/<int:pk>/', views.productlistdetail.as_view(),name="show-detail"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
