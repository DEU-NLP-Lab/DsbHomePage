from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from .validators import *

# Create your models here.

class Picture(models.Model):
    title = models.CharField(max_length=30)
    # content = models.TextField()
    content = CKEditor5Field(config_name="extends", blank=True, null=True, verbose_name='내용')  # CKEditor 5 필드

    image = models.ImageField(upload_to='pictures/image/%Y/%m/%d', blank=False)

    file = models.FileField(
        upload_to='pictures/files/%Y/%m/%d',
        null=True,
        validators=[validate_file_extension, ],
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author: 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}] {self.title}'  # 해당 포스트의 pk 값과 해당 포스트의 title 값
