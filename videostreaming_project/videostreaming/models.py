from django.db import models


from django.contrib.auth.models import User
from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=100)
    video_url = models.URLField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
