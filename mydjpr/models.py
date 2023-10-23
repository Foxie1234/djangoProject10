from django.db import models


class TestModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')

class TestModel2(models.Model):
    title = models.CharField(max_length=50, verbose_name='test Field')

