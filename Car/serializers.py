from django.db.models import fields
from Car.models import Contract
from rest_framework import serializers
from User.models import Base_User
from Car.models import *
class OwnerEditDealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base_User
        fields = '__all__'

class SignContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields='__all__'