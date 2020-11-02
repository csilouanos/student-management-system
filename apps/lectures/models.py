from django.db import models
from apps.utils.models import Timestamps
from django.core.validators import MinValueValidator, MaxValueValidator

class Lecture(Timestamps, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    lecturer_name = models.CharField(max_length=100, default='', blank=True)
    date = models.DateField()
    duration = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(10)], 
                                       help_text='Enter number of hours',
                                       default=1)
    slides_url = models.CharField(max_length=255)
    is_required = models.BooleanField(default=True)