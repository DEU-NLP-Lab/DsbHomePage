from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.

class Results(models.Model):
    image = models.ImageField(upload_to='pictures/results/%Y/%m/%d', blank=False)

    def __str__(self):
        return f'[{self.pk}]'  # 해당 포스트의 pk 값
