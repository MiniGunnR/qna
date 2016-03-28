from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class TimeStamped(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PostAttribute(TimeStamped):
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User)
    anonymous = models.BooleanField(default=False)
    hearts = models.PositiveIntegerField(default=0, blank=True, null=True)
    flags = models.PositiveIntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True


class CommentCount(models.Model):
    comments = models.PositiveIntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True


class QuestionChild(models.Model):
    parent = models.ForeignKey('Question')

    class Meta:
        abstract = True


class AnswerChild(models.Model):
    parent = models.ForeignKey('Answer')

    class Meta:
        abstract = True


class QuestionPoint(TimeStamped):
    question = models.ForeignKey('Question')
    user = models.ForeignKey(User)

    class meta:
        unique_together = ('question', 'user')
        abstract = True


class AnswerPoint(TimeStamped):
    answer = models.ForeignKey('Answer')
    user = models.ForeignKey(User)

    class meta:
        unique_together = ('answer', 'user')
        abstract = True


class QuestionCommentPoint(TimeStamped):
    comment = models.ForeignKey('QuestionComment')
    user = models.ForeignKey(User)

    class meta:
        unique_together = ('comment', 'user')
        abstract = True

class AnswerCommentPoint(TimeStamped):
    comment = models.ForeignKey('AnswerComment')
    user = models.ForeignKey(User)

    class meta:
        unique_together = ('comment', 'user')
        abstract = True
