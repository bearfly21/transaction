from .models import *
from rest_framework import serializers

class TransactionSerializer(serializers.ModelSerializer):
    model = Transaction
    fields = '__all__'