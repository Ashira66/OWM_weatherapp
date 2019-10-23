from django.db import models
from django.utils import timezone

class weatherdata(models.Model):
    Location = models.CharField(max_length=50)0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def weather_data(self):
        return '%s'%(self.Location)

    def __str__(self):
        return self.weather_data()
