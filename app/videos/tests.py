from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from users.models import User
from videos.models import Video

from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile # 파일 관련 테스트할때 사용

# Create your tests here.
# views에 API 구조를 일단 잡아놨다면,
# 여기에서 테스트 주도 기반 개발방식 적용
class VideoAPITest(APITestCase):

    # 테스트 코드가 실행되기 전 가장 먼저 실행되는 함수
    # 테스트 하기 전에, 데이터를 미리 생성해두는 역할
    # (1) - User 생성 및 로그인
    # (2) - Video 생성
    def setUp(self):
        # 유저 생성
        self.new_user = User.objects.create_user(
            email="test@test.com",
            password="123123"
        )
        # 로그인
        self.client.login(email="test@test.com", password="123123")

        # Video 생성
        self.new_video = Video.objects.create(
            user = self.new_user,
            title = "test video!!",
            description = "test",
            link="www.test.com",
            category="test",
            views_count="34",
            video_file=SimpleUploadedFile('test.mp4', b'file_content', content_type='video/mp4'),
            thumbnail="www.test.com",
        )

    # api/v1/videos [GET]
    def test_video_list_get(self):
        url = reverse('video_list')
        # url로 GET 요청 전송
        result = self.client.get(url)

        # 검증
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertTrue(len(result.data) > 0)

        for video in result.data:
            self.assertIn('title', video)

    # api/v1/videos [POST]
    def test_video_list_post(self):
        url = reverse('video_list')

        data = {
            'title': 'My test video 2',
            'description': 'test 2',
            'link': 'http://www.test.com',
            'category': 'development',
            'thumbnail': 'http://www.test.com',
            'video_file': SimpleUploadedFile('test.mp4', b'file_content', content_type='video/mp4'),
            'user': self.new_user.pk,
            'views_count': 1234,
        }

        # url로 POST 요청 전송
        result = self.client.post(url, data)

        # 검증
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result.data['title'], 'My test video 2')
        self.assertEqual(result.data['category'], 'development')

    # api/v1/videos/{video_id} [GET]
    def test_video_detail_get(self):
        url = reverse('video_detail', kwargs={'pk': self.new_video.id})

        # url로 GET 요청 전송
        result = self.client.get(url)

        # 검증
        self.assertEqual(result.status_code, status.HTTP_200_OK)

    # api/v1/videos/{video_id} [PUT]
    def test_video_detail_put(self):
        url = reverse('video_detail', kwargs={'pk': self.new_video.id})

        data = {
            'title': 'Updated test video',
            'description': 'test put',
            'link': 'http://www.test.com',
            'category': 'development',
            'thumbnail': 'http://www.test.com',
            'video_file': SimpleUploadedFile('test.mp4', b'file_content', content_type='video/mp4'),
            'user': self.new_user.pk,
            'views_count': 1111,
        }

        # url로 POST 요청 전송
        result = self.client.put(url, data)

        # 검증
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['title'], 'Updated test video')
        self.assertEqual(result.data['views_count'], 1111)

    # api/v1/videos/{video_id} [DELETE]
    def test_video_detail_delete(self):
        url = reverse('video_detail', kwargs={'pk': self.new_video.id})

        # url로 DELETE 요청 전송
        # 이미 로그인한 유저로 요청을 보내는것이므로, 따로 처리안해도 됨
        result = self.client.delete(url)

        # 검증
        self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)

        result = self.client.get(url)
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)
