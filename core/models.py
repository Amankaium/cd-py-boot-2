from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='products'
    )
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(default=1)
    product_image = models.ImageField(upload_to="products", null=True, blank=True)


