from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib


class Data(models.Model):
    pressure = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10000000)], null=True)
    max_temp = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10000000)], null=True)
    temp = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10000000)], null=True)
    min_temp = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10000000)], null=True)
    dewpoint = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10000000)], null=True)
    humidity = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10000000)], null=True)
    cloud = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10000000)], null=True)
    sunshine = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10000000)], null=True)
    wind_direction = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10000000)], null=True)
    wind_speed = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10000000)], null=True)
    rain_fall = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/rain_prediction_lineair_model.joblib')
        self.rain_fall = ml_model.predict([[self.pressure, self.max_temp, self.temp,  self.min_temp,  self.dewpoint, self.humidity, self.cloud, self.sunshine, self.wind_direction, self.wind_speed ]])
        return super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.date