from django.db import models

from django.db.models import Manager


class SupplierQuerySet(models.QuerySet):
    """
    QuerySet класс, который фильтрует Supplier, UniqueBuyersSuppliers, SupplierCarModel модель.
    """

    def for_supplier(self, supplier=None, user=None) -> Manager[models.Model]:
        if user:
            return self.filter(user_id=user, is_active=True)
        else:
            return self.filter(supplier_id=supplier, is_active=True)
