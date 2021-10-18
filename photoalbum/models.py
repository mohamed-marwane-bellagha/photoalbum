import datetime

from django.db import models
from django.utils import timezone

class Image(models.Model):
    image_name = models.FileField(upload_to='photoalbum/static/photoalbum/image/')
    filename=models.CharField( max_length=500)
    date_published = models.DateTimeField('date published')
    def __str__(self):
            return self.image_name ;

    def was_published_recently(self):
        return self.date_published >= timezone.now() - datetime.timedelta(days=1)
# Create your models here.
