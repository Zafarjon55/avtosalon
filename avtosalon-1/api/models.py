from django.db import models

# Create your models here.


class Dealer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.manufacturer} {self.name} {self.year}"

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.ForeignKey(CarModel, related_name='cars', on_delete=models.CASCADE)
    dealer = models.ForeignKey(Dealer, related_name='cars', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField(null=True)
    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return self.name