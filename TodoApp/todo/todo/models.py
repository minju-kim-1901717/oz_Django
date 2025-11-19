from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Todo(models.Model):
    category_choices = (
        ('life','일상'),
        ('hobby','취미'),
        ('want','버킷리스트'),

    )
    category = models.CharField(max_length=20, choices=category_choices, default='life')
    title = models.CharField('title',max_length=100)
    detail = models.TextField('detail')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created = models.DateTimeField('작성일자',auto_now_add=True)
    updated = models.DateTimeField('수정일자',auto_now=True)

    def __str__(self):
        return f'{self.title[:10]}'


    class Meta:
        verbose_name = '할일'
        verbose_name_plural = '상세'
