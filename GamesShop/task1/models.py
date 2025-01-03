from collections import defaultdict

from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100)  # Имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # баланс
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)  # Название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    size = models.DecimalField(max_digits=10, decimal_places=2)  # размер файлов игры
    description = models.TextField()  # Описание игры
    age_limited = models.BooleanField(default=False)  # ограничение возраста 18+
    buyer = models.ManyToManyField(Buyer, related_name='games')  # Связь с покупателем

    def __str__(self):
        return self.name
