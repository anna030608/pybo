from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 이게 바로 ORM code 이다...
# SQL이 자동으로 생성됨...


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject
    ## 그 id의 질문의 내용의 title이 보여다..


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ## CASCADE : 질문이 사라지면 답변도  같이 사라짐.
    content = models.TextField()
    create_date = models.DateTimeField()
    # Answer은 3개지의 필드가 있다...이 만족시켜야 한다...
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

    def __str__(self):
        return self.content

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
