from django.db import models


class Uzum(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qoshimcha = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name