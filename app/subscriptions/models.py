from django.db import models
from common.models import Common


class Subscription(Common):
    # 내 채널을 구독한 사람
    subscriber = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscribed_channels')

    # 내가 구독한 채널
    subscribed_channel = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscribers')
