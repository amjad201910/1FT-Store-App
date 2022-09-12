from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product , Photo
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'pk']
class PhotoSerializerEdit(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ['pk','Image','Color', 'Cover']
class PhotoSerializerAddNew(serializers.ModelSerializer):
    class Meta:

        model = Photo
        fields = ['pk','product','Image','Color', 'Cover']

    def create(self, validated_data):
            try:
             return  super().create(validated_data)
            except:
               raise serializers.ValidationError("you have more than one cover ")




class PhotoSerializershowDetail(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ['Color', 'Image']
class PhotoSerializershow(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = [ 'Image']

class ProductSerializerShow(serializers.HyperlinkedModelSerializer):
   # #url = serializers.SerializerMethodField(read_only=True)
   # url=serializers.HyperlinkedIdentityField(view_name='show-detail',lookup_field='pk',read_only=True)
    #photos=PhotoSerializershow(source='photo_set.filter(Cover=False)',read_only=True,many=True)
    photo=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ['Body','pk','Name','Type','Price','photo']
    def get_photo(self,obj):
        photo=obj.photo_set.get(Cover=True)
        print("////////////////////////////////////////////////////////////////////////////")
        print(self.context)
        p = PhotoSerializershow(photo, context=self.context).data
        return p['Image']

    #def get_url(self,obj):
     #   request=self.context.get('request')
      #  if request is None:
       #     return None
        #return reverse("show-detail",kwargs={"id": obj.pk},request=request)



class ProductSerializerShowDetail(serializers.HyperlinkedModelSerializer):
    photos=PhotoSerializershowDetail(source='photo_set.all',read_only=True,many=True)
    class Meta:
        model = Product
        fields = ['pk', 'Name', 'Body', 'Type', 'Price', 'Quantity', 'Created_on','photos']
class ProductSerializerUpdate(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ['pk', 'Name', 'Body', 'Type', 'Price', 'Quantity', 'Created_on']




class ProductSerializerEdit(serializers.HyperlinkedModelSerializer):
    photos = PhotoSerializerEdit(write_only=True,many=True)#many
    class Meta:
        model = Product
        fields = ['pk', 'Name', 'Body', 'Type', 'Price', 'Quantity', 'Created_on','photos']

    def create(self, validated_data):
      print("?????????????????????????????????????????????????????????????????")
      print(self)
      images_data = validated_data.pop('photos')
      product_data = super().create(validated_data)

     # for imagedata in imagesdata:
      print(type(images_data))
      #images_data['product']=product_data.pk
      #PhotoSerializerAddNew.create(self,images_data)
      print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
      photos=PhotoSerializerAddNew(data=images_data,many=True)
      print("lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")
      if photos.is_valid(raise_exception=True):
         photos.save(product=product_data)
      #else:
       #   raise serializers.ValidationError("error in photo ")

      return validated_data
    def validate_photo(self, value):
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print(self.context['request'].data)
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

        photo_cover=Photo.objects.filter(Product=value.Product).filter(Cover=True)
        if value['Cover'] == True and photo_cover.exists() :

            raise serializers.ValidationError("you have more than one cover ")