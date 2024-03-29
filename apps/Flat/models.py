from django.db import models

class Flats(models.Model):
    class Currency(models.TextChoices):
        dollar = "$"


    img = models.ImageField(
        blank=True,
        upload_to="flat / "
        
    )
    title = models.CharField(
        max_length=250, verbose_name="Название"
    )

    description = models.TextField(
        verbose_name="Описание"
    )
    bedrooms = models.PositiveIntegerField(
        verbose_name="Спальня"
    )
    bathrooms = models.PositiveIntegerField(
        verbose_name="Ванная"
    )
    m2 = models.PositiveIntegerField(
        verbose_name="Квадратные метры"
    )
    location = models.CharField(
        max_length=255,
        verbose_name="Местоположение"
    )
    price = models.FloatField(
        verbose_name="Цена"
    )

    class Meta:
        verbose_name = "Flat"
        verbose_name_plural = "Flats"
    
    def __str__(self) -> str:
        return self.title