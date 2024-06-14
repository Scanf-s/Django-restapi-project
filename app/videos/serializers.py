from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer
from .models import Video


class VideoListSerializer(ModelSerializer):

    user = UserSerializer(read_only=True) # video에서 user를 modify하지 않기 때문에, read_only=True로 설정한다.

    class Meta:
        model = Video
        fields = '__all__'
