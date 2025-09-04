from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Transaction.objects.filter(user=self.request.user)
        type = self.request.query_params.get('type')
        start_date = self.request.query_params.get('start')
        end_date = self.request.query_params.get('end')
        search = self.request.query_params.get('search')

        if type:
            queryset = queryset.filter(type__name=type)
        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])
        if search:
            queryset = queryset.filter(
                Q(description__icontains=search) | Q(category__icontains=search)
            )
        return queryset
