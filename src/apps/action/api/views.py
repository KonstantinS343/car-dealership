from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.db.models import BaseManager

from .serializers import ActionCarDealershipSerializer
from apps.action.models import ActionCarDealership


class ActionCarDealershipViewSet(viewsets.GenericViewSet):
    """
    ViewSet для работы с акциями автомобильного дилера.

    Этот ViewSet обеспечивает функциональность для работы с акциями автомобильного дилера.
    Он предоставляет набор действий для создания, обновления, удаления и просмотра акций.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = ActionCarDealershipSerializer

    def get_queryset(self) -> BaseManager[ActionCarDealership]:
        """
        Возвращает queryset, модели ActionCarDealership.

        Фильтруем и возвращаем акции текущего пользователя (представитель автосалона), которые активны, т.е. не были удалены.
        """
        return ActionCarDealership.objects.filter(car_dealership__user=self.request.user.id, is_active=True)

    def list(self, request):
        """
        Возвращаем список акции текущего пользователя (представитель автосалона).
        """
        actions = self.get_queryset()
        serializer = self.get_serializer(actions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
