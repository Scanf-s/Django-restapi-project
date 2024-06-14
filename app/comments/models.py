from django.db import models
from common.models import Common
# Create your models here.

class Comment(Common):
    # User 1명은 여러개의 Comment를 작성할 수 있음 (1:N관계) -> Comment에 FK 작성 (Comment가 User를 여러명 가질 수 있는 경우? -> 이건 아님)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='comments')

    # Video 1개는 여러개의 Comment를 가질 수 있음  (1:N관계) -> Comment에 FK 작성
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE, related_name='comments')

    content = models.TextField()

    # 댓글에 대한 좋아요, 싫어요 반응 필드
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

    # 대댓글
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
