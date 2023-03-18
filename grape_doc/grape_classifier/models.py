from django.db import models


# Create your models here.
class GrapeClassification(models.Model):
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.FileField(upload_to='uploads/', blank=True)
