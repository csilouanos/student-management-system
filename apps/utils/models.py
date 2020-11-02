from django.db import models

class Timestamps(models.Model):
    #auto_now_add only creates the timestamp when is created
    created_at = models.DateField(auto_now_add=True)
    #auto_now every time is updated
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True
