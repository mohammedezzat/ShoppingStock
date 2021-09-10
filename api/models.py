from django.db import models

# Create your models here.

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    gtin = models.CharField(max_length=14)
    shop = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expirydate = models.DateField()
    class Meta:
        unique_together = ['gtin','shop','expirydate']
