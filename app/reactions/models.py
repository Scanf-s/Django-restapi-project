from django.db import models
from common.models import Common

# Create your models here.
class Reaction(Common):

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0
    REACTION_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
        (NO_REACTION, 'No Reaction')
    )

    # 좋아요, 싫어요같은 반응 데이터를 받는 필드 ( 1 : Like, -1 : Dislike, 0: No Reaction)
    reaction = models.IntegerField(choices=REACTION_CHOICES, default=NO_REACTION)

    # User 1명은 여러개의 Reaction을 할 수 있음 (1:N관계) -> Reaction에 FK 작성
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='reactions')
    # Video 1개는 여러개의 Reaction을 가질 수 있음. (1:N관계) -> Reaction에 FK 작성
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE, related_name='reactions')

    class Meta:
        db_table = 'reactions'
