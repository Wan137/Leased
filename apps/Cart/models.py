from django.db import models

from apps.Flat.models import Flats
from apps.User.models import User

   
class Cart(models.Model):
    flats_id = models.ForeignKey(
        Flats, on_delete=models.CASCADE,
        related_name="cart_flats", verbose_name="Квартиры"
    )
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="cart_users", verbose_name="Пользователь"
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f"{self.user_id} - {self.flats_id}"