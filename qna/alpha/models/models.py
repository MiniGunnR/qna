from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from abstracts import TimeStamped, PostAttribute, CommentCount, QuestionChild, AnswerChild, \
    QuestionPoint, AnswerPoint, QuestionCommentPoint, AnswerCommentPoint


class Category(TimeStamped):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)
    usage = models.PositiveIntegerField(default=0, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class Question(PostAttribute, CommentCount):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    closed = models.BooleanField(default=False)
    answers = models.PositiveIntegerField(default=0, blank=True, null=True)
    followers = models.PositiveIntegerField(default=0, blank=True, null=True)

    def __unicode__(self):
        return self.title


class Answer(PostAttribute, CommentCount, QuestionChild):

    def __unicode__(self):
        return self.body


class QuestionComment(PostAttribute, QuestionChild):

    def __unicode__(self):
        return self.body


class AnswerComment(PostAttribute, AnswerChild):

    def __unicode__(self):
        return self.body


class QuestionHeart(QuestionPoint):

    class Meta:
        verbose_name_plural = 'X: Hearts -> Question'

    def __unicode__(self):
        return "%s - %s" % (self.user, self.question)


class QuestionFlag(QuestionPoint):

    class Meta:
        verbose_name_plural = 'X: Flags -> Question'

    def __unicode__(self):
        return "%s - %s" % (self.user, self.question)


class AnswerHeart(AnswerPoint):

    class Meta:
        verbose_name_plural = 'X: Hearts -> Answer'

    def __unicode__(self):
        return "%s - %s" % (self.user, self.answer)


class AnswerFlag(AnswerPoint):

    class Meta:
        verbose_name_plural = 'X: Flags -> Answer'

    def __unicode__(self):
        return "%s - %s" % (self.user, self.answer)


class QuestionCommentHeart(QuestionCommentPoint):

    class Meta:
        verbose_name_plural = 'X: Hearts -> Question Comment'

    def __unicode__(self):
        return "%s - %s" % (self.user, self.comment)


class QuestionCommentFlag(QuestionCommentPoint):

    class Meta:
        verbose_name_plural = 'X: Flags -> Question Comment'

    def __unicode__(self):
        return "%s - %s" % (self.user, self.comment)


class AnswerCommentHeart(AnswerCommentPoint):

    class Meta:
        verbose_name_plural = 'X: Hearts -> Answer Comment'

    def __unicode__(self):
        return "%s - %s" % (self.user, self.comment)


class AnswerCommentFlag(AnswerCommentPoint):

    class Meta:
        verbose_name_plural = 'X: Flags -> Answer Comment'

    def __unicode__(self):
        return "%s - %s" % (self.user, self.comment)


class NotificationObject(TimeStamped):
    action_choices = (
        ('A', 'wrote an answer to your question.'),
        ('QC', 'commented on your question.'),
        ('AC', 'commented on your answer.'),
        ('QH', 'liked your answer.'),
        ('AH', 'liked your answer.'),
    )
    action = models.CharField(max_length=2,
                              choices=action_choices,
                              default='A')
    url = models.CharField(max_length=200, default='')


class NotificationDetail(TimeStamped):
    obj = models.ForeignKey('NotificationObject')
    actor = models.ForeignKey(User)
    isRead = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='my_notifications')

    def __unicode__(self):
        return "%s %s -> %s" % (self.actor, self.get_action_display(), self.user)


class Notification(TimeStamped):
    primary_actor = models.CharField(max_length=50)
    extra_actors = models.CharField(max_length=50, default='') # follow values for this field with a space
    action = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s %s%s" % self.primary_actor, self.extra_actors, self.action


class QuestionFollowers(QuestionPoint):

    class Meta:
        verbose_name_plural = 'X: Follows -> Question'

    def __unicode__(self):
        return "%s following %s" % (self.user, self.question)
