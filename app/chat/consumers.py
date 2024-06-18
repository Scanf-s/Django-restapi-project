import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

# Synchronous version of WebsocketConsumer
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         """
#         새로운 WebSocket 연결이 수립되었을 때 호출된다.
#         """
#         # URL 경로에서 'room_name' 인자를 가져와 방 이름을 설정합니다.
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         # 그룹 이름을 생성합니다. 방 이름을 이용해 유니크한 그룹 이름을 만듭니다.
#         self.room_group_name = f"chat_{self.room_name}"
#
#         # 방 그룹에 가입합니다.
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name, self.channel_name
#         )
#
#         # WebSocket 연결을 수락합니다.
#         self.accept()
#
#     def disconnect(self, close_code):
#         # 방 그룹에서 탈퇴합니다.
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name, self.channel_name
#         )
#
#     # WebSocket으로부터 메시지를 받습니다.
#     def receive(self, text_data):
#         # 수신한 텍스트 데이터를 JSON 형식으로 변환합니다.
#         text_data_json = json.loads(text_data)
#         # JSON 데이터에서 메시지를 추출합니다.
#         message = text_data_json["message"]
#
#         # 방 그룹에 메시지를 보냅니다.
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name, {"type": "chat.message", "message": message}
#         )
#
#     # 방 그룹으로부터 메시지를 받습니다.
#     def chat_message(self, event):
#         # 이벤트에서 메시지를 추출합니다.
#         message = event["message"]
#
#         # WebSocket으로 메시지를 보냅니다.
#         self.send(text_data=json.dumps({"message": message}))

class ChatConsumer(AsyncWebsocketConsumer):
    """
    AsyncWebsocketConsumer를 상속받아 WebSocket 연결을 비동기로 처리하는 소비자 클래스입니다.
    모든 메소드는 비동기적으로 정의됩니다.

    채널 계층에서 메서드를 호출할 때 async_to_sync가 더 이상 필요하지 않다.
    """
    async def connect(self):
        """
        새로운 WebSocket 연결이 수립되었을 때 호출됩니다.
        """
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        # await은 Input/Output을 수행하는 비동기 함수를 호출할때 사용한다.
        # AsyncWebsocketConsumer 안에 group_add가 async로 선언되어 있기 때문에 await을 사용해야 한다.
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        # 마찬가지
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))