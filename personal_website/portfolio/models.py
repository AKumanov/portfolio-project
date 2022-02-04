from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='images/', blank=True)
    description = RichTextUploadingField()

    def __str__(self):
        return f'{self.title}'


class Skills(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
