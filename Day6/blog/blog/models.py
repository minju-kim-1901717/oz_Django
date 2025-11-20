from django.contrib.auth import get_user_model
from django.db import models

from utils.models import TimestampedModel

User = get_user_model()


class Blog(TimestampedModel):

    CATEGORY_CHOICES = (
        ('free','자유'),
        ('travel','여행'),
        ('beauty','뷰티'),
    )

    category = models.CharField('카테고리', max_length=20, choices=CATEGORY_CHOICES, default='free')
    title = models.CharField('제목',max_length=100)
    content = models.TextField('본문')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # models.CASCADE -> 같이 삭제됨
    # models.PROJECT -> 삭제가 불가능함(유저를 삭제하려고 할 때 블로그가 있으면 유저삭제 불가능)
    # models.SET_NULL -> 널값 -> 유저 삭제시 블로그 auther가 null이 됨

    #TimestampedModel 사용으로 아래 두줄 필요 없음
    # created = models.DateTimeField('작성일자',auto_now_add=True)
    # updated = models.DateTimeField('수정일자',auto_now=True)

    def __str__(self):
        return f'[{self.get_category_display()}] {self.title[:10]}'

    def get_absolute_url(self):
        return reversed('blog:detail',kwargs={'pk':self.pk})



    class Meta:
        verbose_name = '블로그'
        verbose_name_plural = '블로그목록'


    #블로그 정보
    #댓글 내용
    #작성자
    #작성일자
    #수정일자

class Comment(TimestampedModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.CharField('댓글', max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.blog.title} 본문'

    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = '댓글목록'
        ordering = ('-created','-id')