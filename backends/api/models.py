from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def get_price_in_fcfa(self):
        return f'{self.price} FCFA'
    def get_description(self):
        return f'{self.name} - {self.get_price_in_fcfa()}'
    def get_absolute_url(self):
        return reverse("product_api_view_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.name
