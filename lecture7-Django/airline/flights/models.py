from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length = 3) 
    city = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    #origin = models.CharField(max_length = 64)
    origin = models.ForeignKey( Airport, on_delete=models.CASCADE,related_name="departures" )
    # on_delete=models.CASCADE表示，如果删掉一条airport,则对应删掉origin为该airport的所有航班
    #destination = models.CharField(max_length = 64)
    destination = models.ForeignKey( Airport, on_delete=models.CASCADE,related_name="arrivals" )
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.origin} to {self.destination} "

class Passenger(models.Model):
    #增加乘客信息表，是一种多对多的关系
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name = "passengers")#blank=True表示乘客可能没有航班
    
    def __str__(self):
        return f"{self.first}  {self.last}"