from django.urls import path
from .views import VideoListCreate, VideoRetrieveUpdateDestroy

urlpatterns = [
    path('api/videos/', VideoListCreate.as_view(), name='video-list-create'),
    path('api/videos/<int:pk>/', VideoRetrieveUpdateDestroy.as_view(), name='video-detail'),
]