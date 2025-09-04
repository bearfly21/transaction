from django.db import models
from accounts.models import CustomUser

class Type(models.Model):
    income = models.CharField()
    expense = models.CharField()

class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, related_name= 'users_transaction', on_delete=models.CASCADE)
    amount = models.DecimalField( max_digits=10, decimal_places=2)
    type = models.ForeignKey(Type, related_name='types_of_tranzaction', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    category = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.type



