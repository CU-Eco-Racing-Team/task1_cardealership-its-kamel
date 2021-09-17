from django.urls import path,include
from .views import *


app_name = 'Car'

urlpatterns = [
    path('make-owner/<int:id>', MakeOwner.as_view(), name="make-owner"),
    path('owner-dealer-add/', OwnerEditDealerAdd.as_view(), name="owner-edit-dealer-add"),
    path('owner-dealer-remove/<int:id>/', OwnerEditDealerRemove.as_view(), name="owner-edit-dealer-remove"),
    path('sign-contract/', SignContract.as_view(), name="sign-contract"),
    path('sell-car/', SellCar.as_view(), name="sell-car"),
    path('change-price/', ChangePrice.as_view(), name="change-price"),
    path('buy-car/', BuyCar.as_view(), name="buy-car"),
    path('grant-permissions/<int:id>/', GrantOwnerPermission.as_view(), name="grant-permission"),
]