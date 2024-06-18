"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from chat.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app, # ProtocolTypeRouter가 HTTP 연결인 경우 django_asgi_app을 사용하는 곳으로 라우팅해주고
    "websocket": AllowedHostsOriginValidator( # Websockey 연결인 경우 chat/routing에 만든 websocket_urlpatterns를 따르도록 라우팅
        AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
    )
})
