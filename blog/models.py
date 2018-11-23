from django.db import models
from django.utils import timezone

class Post(models.Model):   # 대문자로 시작
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):  # 소문자와 언더스코어 사용해야한다
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title