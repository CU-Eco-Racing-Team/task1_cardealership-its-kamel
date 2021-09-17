from django.db import models
from User.models import Customer,Dealer
# Create your models here.
class Car(models.Model):

    industry = models.ForeignKey('Industry', on_delete=models.SET_NULL, null=True)

    model = models.TextField()

    plate_number = models.IntegerField()
    
    price = models.IntegerField()

    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    payment = models.CharField(max_length=3, choices=(('1','Cash'),('2','Installment')), default='1')

    dealershop = models.ForeignKey('DealerShop', on_delete = models.SET_NULL, null=True)
    
class Industry(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField(null=True)

class DealerShop(models.Model):
    name = models.CharField(max_length=100)
    industry = models.ManyToManyField(Industry)

class Contract(models.Model):
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL, null=True)
    dealer_shop = models.ForeignKey(DealerShop, on_delete=models.SET_NULL, null=True)
    no_of_cars = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    supervisor = models.ForeignKey(Dealer, on_delete=models.SET_NULL, null=True)

