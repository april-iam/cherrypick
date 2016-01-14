from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Img (models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
#    img_path = 1
#   img_bright=2
#    img_sharpness=3
#    img_distortion=4

    def draw_grid(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title