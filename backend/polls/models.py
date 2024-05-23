from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)  # 自增主键
    username = models.CharField(max_length=30, unique=True, null=False)
    user_pwd = models.CharField(max_length=30, null=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.EmailField()
    signature = models.CharField(max_length=150, null=False)
# 定义盒子表
class Box(models.Model):
    box_id = models.AutoField(primary_key=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='host_id')
    descr = models.TextField()

# 定义帖子表
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name='poster')
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='host')
    question = models.TextField(null=False)
    answer = models.TextField()
    is_public = models.BooleanField(default=True)

class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=30, unique=True, null=False)

class with_tag(models.Model):
    with_tag_id = models.AutoField(primary_key=True)
    post_id_with = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_id_with')
    tag_id_with = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tag_id_with')