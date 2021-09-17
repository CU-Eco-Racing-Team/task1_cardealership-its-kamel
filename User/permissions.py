from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_permission(self, request):
        return hasattr(request.user,'owner')

class IsCustomer(BasePermission):
    def has_permission(self, request):
        return hasattr(request.user,'customer')
    
class IsDealer(BasePermission):
    def has_permission(self, request):
        return hasattr(request.user,'dealer')

class IsOwnerDealer(BasePermission):
    def has_permission(self, request):
        return bool(request.user.has_perm('User.can_buy_car') 
                    and request.user.has_perm('User.change_car_price') 
                    and request.user.has_perm('User.sell_car_to_customer')
                    and request.user.has_perm('User.can_sign_contract'))
