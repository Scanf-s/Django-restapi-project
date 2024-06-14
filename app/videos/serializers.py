from rest_framework.serializers import ModelSerializer, SerializerMethodField

from reactions.models import Reaction
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer
from .models import Video


class VideoListSerializer(ModelSerializer):

    user = UserSerializer(read_only=True) # video에서 user를 modify하지 않기 때문에, read_only=True로 설정한다.

    class Meta:
        model = Video
        fields = '__all__'

class VideoDetailSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    # Video:Comment는 1:N관계이므로 Comment에 FK를 설정해놓았음
    # Video에서 Comment를 찾아야 하므로 Reverse Accessor를 사용해야함
    comment_set = CommentSerializer(many=True, read_only=True, source='comments')
    reactions = SerializerMethodField('get_reactions')

    def get_reactions(self, video):
        return Reaction.get_video_reactions(video)

    class Meta:
        model = Video
        fields = '__all__'
