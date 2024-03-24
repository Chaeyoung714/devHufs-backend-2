from django.db import models
from .post_models import Post
from member.models.member_models import Member

class Comment(models.Model):
    body = models.TextField(default="")
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='comment')
    parent = models.ForeignKey('self', null = True, blank = True, on_delete = models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)