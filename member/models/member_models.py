from django.db import models
from board.models.tech_models import Tech
from board.models.job_models import Job

class Member(models.Model):
    name = models.CharField()



class MemberTech(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='post_tech')
    tech = models.ForeignKey(Tech, on_delete=models.CASCADE, verbose_name='기술스택')

class MemberJob(models.Model):
    member = models.ForeignKey(Member, on_delte=models.CASCADE, related_name='post_job')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name='직업군스택')