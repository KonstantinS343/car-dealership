from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db.utils import IntegrityError
from django.db.models import Manager

from .serializers import BuyerSerializer
from .permissions import BuyerPermission
from apps.buyer.models import Buyer


class BuyerViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с покупателями.

    Этот ViewSet обеспечивает функциональность для работы с покупателями.
    Он предоставляет набор действий для создания и просмотра, обновления и удаления покупателей.
    """

    permission_classes = (IsAuthenticated, BuyerPermission)
    serializer_class = BuyerSerializer

    def get_queryset(self) -> Manager[Buyer]:
        return Buyer.objects.filter(user=self.request.user, is_active=True)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except IntegrityError:
            return Response({"detail": "Вы один покупатель!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
