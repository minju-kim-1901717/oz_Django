from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

#제목
#내용
#작성자
#작성일자
#수정일자
#카테고리

class Blog(models.Model):
    CATEGORY_CHOICES = (
        ('free','자유'),
        ('travel','여행'),
        ('beauty','뷰티'),
    )

    category = models.CharField('카테고리', max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField('제목',max_length=100)
    content = models.TextField('본문')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # models.CASCADE -> 같이 삭제됨
    # models.PROJECT -> 삭제가 불가능함(유저를 삭제하려고 할 때 블로그가 있으면 유저삭제 불가능)
    # models.SET_NULL -> 널값 -> 유저 삭제시 블로그 auther가 null이 됨

    created = models.DateTimeField('작성일자',auto_now_add=True)
    updated = models.DateTimeField('수정일자',auto_now=True)

    def __str__(self):
        return f'[{self.get_category_display()}] {self.title[:10]}'


    class Meta:
        verbose_name = '블로그'
        verbose_name_plural = '블로그목록'
