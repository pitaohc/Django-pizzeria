from django.db import models


# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name
