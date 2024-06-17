from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Video

from .serializers import VideoListSerializer, VideoDetailSerializer

class VideoList(APIView):
    """
    Video list 보여주는 API
    api/v1/videos
    GET : 전체 video 조회
    POST : 새로운 video 생성
    """
    def get(self, request):
        data = Video.objects.all() # => QuerySet[Video, ...]

        # objects -> Json 형식 직렬화
        serializer = VideoListSerializer(data, many=True) # QuerySet에 여러개 존재하니까 many=True
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_data = request.data # Json으로 들어왔기 때문에 역직렬화

        serializer = VideoListSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideoDetail(APIView):
    """
    Video 상세 정보 조회하는 API
    api/v1/videos/{video_id}
    GET : 특정 ID의 Video 조회
    POST : X
    PUT : 특정 ID의 Video 업데이트
    DELETE : 특정 ID의 Video 삭제
    """

    def get(self, request, pk):
        # get_object_or_404를 사용하는게 더 편하다
        data = get_object_or_404(Video, id=pk)

        # objects -> Json 형식 직렬화
        serializer = VideoDetailSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        data = get_object_or_404(Video, id=pk)

        request_data = request.data

        serializer = VideoDetailSerializer(instance=data, data=request_data) # 가져온 instance data를 request_data로 update
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        data = get_object_or_404(Video, id=pk)
        data.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
