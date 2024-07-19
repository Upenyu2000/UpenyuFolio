from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.
class Folio(models.Model):
    project_image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    project_description = models.TextField(max_length=500)
    project_url = models.URLField(max_length=500)

    def __str__(self):
        return (f"{self.project_image} "
                f"{self.project_description} {self.project_url}")


class About(models.Model):
    about = models.TextField(max_length=2000)

    def __str__(self):
        return f"{self.about}"


class Stack(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    language_image = models.ImageField(upload_to='images/', blank=True, null=True)
    framework_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.language_image} {self.framework_image}"


class Project(models.Model):
    VIDEO_TYPES = [
        ('youtube', 'YouTube'),
        ('vimeo', 'Vimeo'),
        ('direct', 'Direct Video URL'),
    ]
    video = EmbedVideoField(null=True, blank=True)
    video_type = models.CharField(max_length=10, choices=VIDEO_TYPES, default='youtube')
    description = models.ForeignKey(Folio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description}"
