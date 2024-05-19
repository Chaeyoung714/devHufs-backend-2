from django.db import models
from .tech_models import Tech
from .job_models import Job
from member.models.member_models import Member

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목')
    body = models.TextField(default="",verbose_name='본문')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='작성자', related_name='post')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일자')
    thumbnail_img = models.ImageField(blank=True, null=True, verbose_name='썸네일 이미지 파일')

    like_cnt = models.IntegerField(default=0, verbose_name='좋아요 수')
    bookmark_cnt = models.IntegerField(default=0, verbose_name='북마크 수')
    comment_cnt = models.IntegerField(default=0, verbose_name='댓글 수')


class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_file')
    file = models.FileField(upload_to="", verbose_name='포트폴리오 파일')

class PostLink(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_link')
    link = models.URLField(default="", verbose_name='포트폴리오 링크')

class PostTech(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_tech')
    tech = models.ForeignKey(Tech, on_delete=models.CASCADE, verbose_name='기술스택')

class PostJob(models.Model):
    post = models.ForeignKey(Post, on_delte=models.CASCADE, related_name='post_job')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name='직업군스택')