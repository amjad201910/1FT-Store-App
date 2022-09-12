from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer,PhotoSerializerAddNew,PhotoSerializerEdit,ProductSerializerUpdate, ProductSerializerShow, ProductSerializerShowDetail,ProductSerializerEdit
from rest_framework import generics
from .models import Product, Photo
from rest_framework.response import Response

class dessertlist(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerShow


class dessercreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerEdit

class potoadd(generics.CreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializerAddNew



class productlistdetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerShowDetail




class productupdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerEdit

    def put(self,request, *args, **kwargs):
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print(request.data)
        print("/////////////////////////////////////////////////////")
        print(args)
        print(kwargs)
        images_data = request.data.pop('photos')
        print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
        pk=kwargs.get("pk",None)
        if not pk:
            return Response({"error":"id error"})
        try:
            instance_product=Product.objects.get(pk=pk)
        except:
            return Response({"error":"product q error"})
        print(type(instance_product))
        print(instance_product.Name)
        print("/////////////////////////////////////////////////////")
        print(request.data)
        product_data= ProductSerializerUpdate(instance=instance_product,data=request.data)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        #product_data = super().update(request=request)
        print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        try:
            instance_photos = instance_product.photo_set.all()
        except:
            return Response({"error": "photo q error"})

        print("/////////////////////////////////////////////////////")
        for image_data in images_data:
            for instance_photo in instance_photos:

                photos=PhotoSerializerEdit(instance=instance_photo,data=image_data)
                photos.is_valid(raise_exception=True)
                photos.save()
                break

         #  Photo.objects.filter(product=request.data.pk).filter(pk=images_data.pk).update(product=product_data, **image_data)
        return Response(product_data.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

