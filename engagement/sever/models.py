from django.db import models
from django import forms 
STATUS_CHOICES = (
    (1, ("Class begin")),
    (2, ("Class end")),
    (3, ("engaging")),
    (4, ("disengaging")),
)

# Create your models here.
class student(models.Model):
	name = models.CharField(max_length=200)
	engagement = models.BooleanField(default = False)
	instructor = models.CharField(max_length=200)
	eye_weight = models.DecimalField(max_digits=10, decimal_places=7)
	engagement_weight1 = models.DecimalField(max_digits=10, decimal_places=7)
	engagement_weight2 = models.DecimalField(max_digits=10, decimal_places=7)
	engagement_weight3 = models.DecimalField(max_digits=10, decimal_places=7)
	engagement_weight4 = models.DecimalField(max_digits=10, decimal_places=7)

class raw_reading(models.Model):
	eye_value = models.DecimalField(max_digits=10, decimal_places=7)
	engagement_value1 = models.DecimalField(max_digits=10, decimal_places=7)
	engagement_value2 = models.DecimalField(max_digits=10, decimal_places=7)
	engagement_value3 = models.DecimalField(max_digits=10, decimal_places=7)
	engagement_value4 = models.DecimalField(max_digits=10, decimal_places=7)

class event_table(models.Model):
	students = models.ForeignKey(student, on_delete=models.CASCADE)
	event_type = forms.ChoiceField(choices=STATUS_CHOICES)
	time = models.DateTimeField(auto_now=True)
	value = models.CharField(max_length = 600)
