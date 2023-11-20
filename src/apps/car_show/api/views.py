from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from .serializers import CarShowSerializer
from .permissions import CarShowPermission
from apps.car_show.models import CarShow


class CarShowViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, CarShowPermission)
    serializer_class = CarShowSerializer
    queryset = CarShow.objects.filter(is_active=True)
