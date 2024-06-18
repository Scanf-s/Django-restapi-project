from django.urls import path
from chat import views

urlpatterns = [
    path('', views.index, name='chat_index'),
    path('<str:room_name>/', views.room, name='chat_room'),
]