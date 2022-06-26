from email.mime import image
from django.db import models
from datetime import datetime

FILE_CHOICES = (
    ('Photo', 'Photo'),
    ("Video", 'Video'),
    ('Maqola', 'Maqola'),
    ('News', "News")
)

class Post(models.Model):

    title = models.CharField(max_length=200)
    descriptions = models.TextField()
    type = models.CharField(choices=FILE_CHOICES, max_length=6)
    file = models.FileField(upload_to='media/files')
    tags = models.ManyToManyField("Tag", blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Messages(models.Model):


    sender_email = models.EmailField(max_length=100)
    sender_name = models.CharField(max_length=200)
    sender_message = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.sender_name