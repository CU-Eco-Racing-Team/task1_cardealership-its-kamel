from Car.models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from User.models import *
from rest_framework import generics
from .serializers import *
from django.contrib.auth.models import Permission
from User.permissions import *
# Create your views here.


class MakeOwner(APIView):
    permission_classes = [IsOwner]
    def post(self, request, *args, **kwargs):
            id = kwargs['id']
            dealer = Dealer.objects.get(SSN = id)
            owner  = Owner(user = dealer)
            owner.save()
            dealer.delete()
            
            return Response(
            {
                'success': True,
                'message': 'Make Owner Success'
            })

class OwnerEditDealerAdd(generics.CreateAPIView):
    permission_classes = [IsOwner]
    queryset = Base_User.objects.all()
    serializer_class = OwnerEditDealerSerializer

class OwnerEditDealerRemove(generics.DestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Base_User.objects.all()
    serializer_class = OwnerEditDealerSerializer
    lookup_field = 'id'

class SignContract(APIView):
    permission_classes = [IsOwner|IsOwnerDealer]
    
    def post(self, request, *args, **kwargs):

        industry_id = request.data['industry_id']
        dealershop_id = request.data['dealershop_id']
        supervior_id = request.data['dealer_id']
        
        dealer = Dealer.objects.get(SSN = supervior_id)
        dealershop = DealerShop.objects.get(id = dealershop_id)
        industry = Industry.objects.get(id = industry_id)

        ################3
        serializer = SignContractSerializer(industry = industry, dealer_shop = dealershop, supervisor = dealer,
                                            no_of_cars=request.data['no_of_cars'],start_date=request.data['start_date'],
                                            end_date = request.data['end_date'])
        if serializer.is_valid():
            serializer.save()
            Contract(serializer.data)
            
            return Response(
            {
                'success': True,
                'message': 'Sign Contract Success'
            })

class SellCar(APIView):
    permission_classes = [IsOwner|IsOwnerDealer]
    
    def put(self, request, *args, **kwargs):
        car_id = request.data['car_id']
        customer_id = request.data['customer_id']
        car = Car.objects.get(id = car_id)
        customer = Customer.objects.get(SSN=customer_id)

        car.owner = customer
        car.save()
        return Response(
                {
                    'success': True,
                    'message': 'Sell Car To Customer Success'
                })

class ChangePrice(APIView):
    permission_classes = [IsOwner|IsOwnerDealer]
    
    def put(self, request, *args, **kwargs):
        serializer = CarSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(
                {
                    'success': True,
                    'message': 'Change Car Price Success'
                })

class BuyCar(APIView):
    permission_classes = [IsOwner|IsOwnerDealer]
    
    def post(self, request, *args, **kwargs):
        serializer = CarSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
            return Response(
            {
                'success': True,
                'message': 'Buy Car Success'
            })
        return Response(
            {
                'success': False,
                'message': 'Buy Car Failed'
            })
class GrantOwnerPermission(APIView):
    permission_classes = [IsOwner]
    def post(self, request, *args, **kwargs):
            id = kwargs['id']
            dealer = Dealer.objects.get(SSN = id)
            permission1 = Permission.objects.get(name ='Change car price') 
            permission2 = Permission.objects.get(name ='Can buy cay') 
            permission3 = Permission.objects.get(name ='Sell car to customer') 
            permission4 = Permission.objects.get(name =' Can sign contract') 

            dealer.user.user_permissions.add(permission1)
            dealer.user.user_permissions.add(permission2)
            dealer.user.user_permissions.add(permission3)
            dealer.user.user_permissions.add(permission4)

            dealer.save()

            return Response(
            {
                'success': True,
                'message': 'Permissions Granted'
            })
