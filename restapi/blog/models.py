from django.db import models
from django.utils import timezone


class Post(models.Model):

    class Meta(object):
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    author = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=timezone.now)
    upd_date = models.DateTimeField(auto_now=timezone.now)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.author + ': ' + self.title


class Comment(models.Model):

    class Meta(object):
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    author = models.CharField(max_length=50)
    text = models.TextField()
    post = models.ForeignKey(Post)
    pub_date = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self):
        return self.author + ': ' + self.text
