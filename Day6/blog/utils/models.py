from django.db import models

class  TimestampedModel(models.Model):
    created = models.DateTimeField('작성일자',auto_now_add=True)
    updated = models.DateTimeField('수정일자',auto_now=True)

    class Meta:
        abstract = True