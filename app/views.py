from django.shortcuts import render
from rest_framework import generics
from .serializers import *

class TransactionCreateApiView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetailUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    