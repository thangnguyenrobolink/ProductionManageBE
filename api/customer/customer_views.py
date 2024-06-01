from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.base.custom_pagination import CustomLimitOffsetPagination
from api.customer.customer_model import Customer
from api.customer.customer_serializer import CustomerSerializer


class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = CustomLimitOffsetPagination
    permission_classes = [IsAuthenticated]


class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
