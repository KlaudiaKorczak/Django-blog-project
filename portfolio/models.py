from django.db import models


class Paintings(models.Model):
    image = models.ImageField(upload_to='images/paintings_img/')
    title = models.CharField(max_length=50, blank=True)
    create_date = models.DateField('date published')
    description = models.CharField(max_length=200, blank=True)
    details = models.CharField(max_length=50, blank=True)
