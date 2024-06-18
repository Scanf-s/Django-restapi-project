# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    # ASGI 애플리케이션을 얻기 위해 as_asgi() 클래스 메서드를 호출
    # Django의 as_view()와 유사한 기능을 수행함.
]