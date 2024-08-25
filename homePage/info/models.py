from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class Info(models.Model):
    title = models.CharField(max_length=30, verbose_name='제목')

    content = CKEditor5Field(config_name="extends", blank=True, null=True, verbose_name='내용')  # CKEditor 5 필드

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='최근 수정일')

    # author: 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}] {self.title}'  # 해당 포스트의 pk 값과 해당 포스트의 title 값
