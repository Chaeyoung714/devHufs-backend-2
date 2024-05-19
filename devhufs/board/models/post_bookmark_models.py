from django.db import models
from .post_models import Post
from member.models.member_models import Member

class PostBookmark(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='bookmark')