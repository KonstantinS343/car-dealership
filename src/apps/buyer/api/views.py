from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db.utils import IntegrityError
from django.db.models import Manager

from .serializers import BuyerSerializer, BuyerUpdateSerializer
from .permissions import BuyerPermission
from apps.buyer.model.models import Buyer


class BuyerViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с покупателями.

    Этот ViewSet обеспечивает функциональность для работы с покупателями.
    Он предоставляет набор действий для создания и просмотра, обновления и удаления покупателей.
    """

    permission_classes = (IsAuthenticated, BuyerPermission)

    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'partial_update':
            return BuyerUpdateSerializer
        else:
            return BuyerSerializer

    def get_queryset(self) -> Manager[Buyer]:
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return Buyer.objects.none()
        return Buyer.objects.for_buyer(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save(user_id=self.request.user.id)
        except IntegrityError:
            return Response({"detail": "Вы один покупатель!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
