from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar/',null=False, blank=False)
    description = models.CharField(max_length=512, null=False, blank=False)
    
    class meta:
        db_table = 'profiles'
        verbose_name = ('Profile')
        verbose_name_plural = ('Profiles')
        
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    caption = models.TextField(max_length=512)
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


class PostFile(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    file = models.FileField(upload_to= 'file/post_file',)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'PostFiles'
        verbose_name = 'Post File'
        verbose_name_plural = 'Post Files'


class Like(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.PROTECT, related_name='likes')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Likes'
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.PROTECT, related_name='comments')
    text = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'



    