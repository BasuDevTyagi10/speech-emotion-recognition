from django.db import models

# Create your models here.
class AudioFileModel(models.Model):
    filepath = models.FileField(upload_to='media/')