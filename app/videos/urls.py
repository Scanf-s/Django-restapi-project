from django.urls import path
from videos import views

urlpatterns = [
    path('', views.VideoList.as_view(), name='video_list'),
    path('<int:pk>/', views.VideoDetail.as_view(), name='video_detail'),
]