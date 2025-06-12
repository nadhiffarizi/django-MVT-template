from django.db import models

# Create your models here.
class Tour(models.Model):
    # origin country, destination, number of days, price
    origin_country = models.CharField(max_length=100)
    destination_country = models.CharField(max_length=100)
    number_of_days = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # string representation of the model
    def __str__(self):
        return f"{self.pk}  {self.origin_country} to {self.destination_country} - {self.number_of_days} days - ${self.price}"
