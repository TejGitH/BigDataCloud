from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Incentive(models.Model):
    MINIMUM_ORDERS = 5
    MAXIMUM_ORDERS = 10

    username = models.ForeignKey(
        'customerApi.Customer',
        on_delete=models.CASCADE,
        related_name='incentives'
    )
    order_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = _('incentive')
        verbose_name_plural = _('incentives')

    def __str__(self):
        return f'{self.username} ({self.order_count} orders)'

    def save(self, *args, **kwargs):
        self.order_count = self.username.orders.count()
        if self.order_count >= Incentive.MINIMUM_ORDERS and self.order_count <= Incentive.MAXIMUM_ORDERS:
            self.username.add_points(10)
        elif self.order_count > Incentive.MAXIMUM_ORDERS:
            self.username.add_points(20)
        super().save(*args, **kwargs)
