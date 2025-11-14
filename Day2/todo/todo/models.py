from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField('해야할일', max_length=100)
    detail = models.CharField('상세', max_length=200)
    created_at = models.DateTimeField('생성일시',auto_now_add=True)
    updated_at = models.DateTimeField('수정일시',auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'todo'
        verbose_name_plural = 'todolist'