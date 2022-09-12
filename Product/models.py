from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django_extensions.validators import HexValidator
import uuid
from rest_framework.response import Response
from rest_framework import status
def upload_path(instance, filname):
    now = datetime.now()
    date_time = now.strftime("%m%d%Y%H%M%S")
    return '/'.join([str(uuid.uuid4()),str(date_time), str(instance.product.Name), filname])
class Product(models.Model):

    type_choices = [
        ('Used', 'used'),
        ('New', 'new'),
        ('Open Box', 'open box'),
    ]
    Name = models.CharField(max_length=42)
   # Image=models.ImageField(upload_to=upload_path, blank=True, null=True)
    Body = models.TextField()
    Type = models.CharField(max_length=8, choices=type_choices, default='New')
    Available=models.BooleanField(default=True, blank=True)
    Price=models.FloatField(default=0.00,validators=[MinValueValidator(0.01)])
   # Rate = models.IntegerField( default=0 ,validators=[MinValueValidator(1), MaxValueValidator(5)])
    Quantity = models.BigIntegerField(default=0,validators=[MinValueValidator(1)])
    Created_on = models.DateField(auto_now_add=True, blank=True)
class Photo (models.Model) :
   # Name = models.CharField(max_length=42,default="sa")
    Color = models.CharField(max_length=6, validators=[HexValidator(length=6)])
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
    Image=models.ImageField(upload_to=upload_path, blank=True, null=True)
    Cover=models.BooleanField(default=False)

    def save(self,*args,**kwargs):


       prod = Product.objects.get(pk=self.product.pk)

       photo_cover = prod.photo_set.all().filter(Cover=True)
      # photo_cover =Photo.objects.filter(Product=value.Product).filter(Cover=True)
       if self.Cover == True and photo_cover.exists():
           raise Exception() # ######special Exception

       super().save(*args, **kwargs)
def photo(instance,*args,**kwargs):

    p=Product.objects.get(pk=instance.product.pk)
    print(p.pk)
    print("////////////////////////////////////////////////////")
    photo_cover =p.photo_set.all().filter(Cover=True)
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxx")
   # photo_cover =Photo.objects.filter(Product=value.Product).filter(Cover=True)
    if instance.Cover == True and photo_cover.exists():
        try:
            raise Exception()
        except:
          raise Response({'error': 'you have more than one cover'}, status=status.HTTP_400_BAD_REQUEST)
    print("////////////////////////////////////////////////////")