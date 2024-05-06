from django.db import models

class Clothing(models.Model):
    version = models.CharField(max_length=100)
    type = models.CharField(max_length=200)
    serial_no = models.DecimalField(max_digits=5, decimal_places=2)
    mfg_date = models.DateField()
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.version
