from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


class Contest(models.Model):
    title = models.CharField(
        'Название',
        max_length=20
    )
    description = models.TextField(
        'Описание',
        max_length=20
    )
    price = models.IntegerField(
        'Цена',
        help_text='Рекомендованная розничная цена',
        validators=[
            MinValueValidator(10),
            MaxValueValidator(100)
        ]
    )
    comment = models.TextField(
        'Комментарий',
        max_length=20,
        blank=True,
    )
