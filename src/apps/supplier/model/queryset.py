from django.db import models

from django.db.models import Manager


class SupplierQuerySet(models.QuerySet):
    """
    QuerySet класс, который фильтрует Supplier, UniqueBuyersSuppliers, SupplierCarModel модель.
    """

    def get_supplier_by_id(self, supplier) -> Manager[models.Model]:
        return self.filter(supplier_id=supplier, is_active=True)

    def get_supplier_by_user_id(self, user) -> Manager[models.Model]:
        return self.filter(user_id=user, is_active=True)
