from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Категория')
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=20, verbose_name='Подкатегория')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=20, verbose_name='Тип')

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=20, verbose_name='Статус')

    def __str__(self):
        return self.name
