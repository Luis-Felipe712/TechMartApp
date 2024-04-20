from django.db import models
from uuid import uuid4

class Product(models.Model):
    
    id_product = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Produto: {self.name} | descricao: {self.description}'