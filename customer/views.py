from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Customer, AccountDetails, Arrears
from .serializer import  CustomerSerializer,AccountDetailsSerializer, ArrearsSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes = [IsAuthenticated])
    def me(self,request):
        (customer, created) = Customer.objects.get_or_create(user_id = request.user.id)
        if request.method == 'GET': 
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)




class AccountDetailsViewSet(ModelViewSet):
    queryset = AccountDetails.objects.prefetch_related('customer').all()
    serializer_class = AccountDetailsSerializer
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['GET','PUT'], permission_classes =[IsAuthenticated])
    def me(self, request):
        (customer, created) = Customer.objects.get_or_create(user_id = request.user.id)
        (account , created)= AccountDetails.objects.get_or_create(customer_id = customer.id)

        if request.method == 'GET':
            serializer = AccountDetailsSerializer(account)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = AccountDetailsSerializer(account, request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)