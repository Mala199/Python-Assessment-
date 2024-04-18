from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Video

class VideoTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = APIClient()

    def test_create_video(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/videos/', {'name': 'Test Video', 'video_url': 'https://example.com/video.mp4'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Video.objects.count(), 1)
        self.assertEqual(Video.objects.get().name, 'Test Video')

    def test_retrieve_video(self):
        video = Video.objects.create(name='Test Video', video_url='https://example.com/video.mp4', uploaded_by=self.user)
        response = self.client.get(f'/api/videos/{video.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Video')