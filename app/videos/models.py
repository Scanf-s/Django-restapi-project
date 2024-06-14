from django.db import models
from common.models import Common

# Create your models here.
class Video(Common):
    title = models.CharField(max_length=30)
    description = models.TextField()
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField() # S3에 업로드 -> 저장 -> URL 리턴값 받음
    video_file = models.FileField(upload_to='storage/')

    # User 1명은 여러개의 Video를 업로드할 수 있음. (1:N관계) -> 자녀 Model에 FK 작성
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='videos')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'videos'