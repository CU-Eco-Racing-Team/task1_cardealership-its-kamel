from django.db import models
from django.contrib.auth.models import AbstractUser

class Base_User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField(null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Owner(models.Model):
    user = models.OneToOneField('Base_User',on_delete= models.CASCADE)
    SSN = models.AutoField(primary_key=True)
    # dealer_shop = models.OneToOneField('DealerShop', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        permissions = [('can_buy_car', 'Can buy car'),
                       ('change_car_price','Change car price'),
                       ('sell_car_to_customer','Sell car to customer'),
                       ('can_sign_contract', 'Can sign contract'),]
class Dealer(models.Model):
    user = models.OneToOneField('Base_User',on_delete= models.CASCADE)
    SSN = models.AutoField(primary_key=True)
    # dealer_shop = models.ForeignKey(DealerShop, on_delete=models.SET_NULL, null=True)
    

class Customer(models.Model):
    user = models.OneToOneField('Base_User',on_delete= models.CASCADE)
    SSN = models.AutoField(primary_key=True)
