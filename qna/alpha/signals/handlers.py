from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

from ..models.models import Question, Answer, QuestionComment, AnswerComment, QuestionHeart, QuestionFlag, \
    AnswerHeart, AnswerFlag, QuestionCommentHeart, QuestionCommentFlag, AnswerCommentHeart, AnswerCommentFlag, \
    NotificationObject, NotificationObjectActor


# # # ADD AND REMOVE QUESTION COUNT IN THE CATEGORY MODEL # # #
@receiver(post_save, sender=Question)
def add_ques_count_to_category(instance, created, **kwargs):
    if created:
        instance.category.usage += 1
        instance.category.save()

@receiver(post_delete, sender=Question)
def rem_ques_count_from_category(instance, **kwargs):
    instance.category.usage -= 1
    instance.category.save()
# # # --------------------------------------------------- # # #

# # # ADD AND REMOVE ANSWER COUNT IN THE QUESTION MODEL # # #
@receiver(post_save, sender=Answer)
def add_ans_count_to_question(instance, created, **kwargs):
    if created:
        instance.parent.answers += 1
        instance.parent.save()

@receiver(post_delete, sender=Answer)
def rem_ans_count_from_question(instance, **kwargs):
    instance.parent.answers -= 1
    instance.parent.save()
# # # --------------------------------------------------- # # #

# # # ADD AND REMOVE QUESTION COMMENT COUNT IN THE QUESTION MODEL # # #
@receiver(post_save, sender=QuestionComment)
def add_ques_comment_count_to_question(instance, created, **kwargs):
    if created:
        instance.parent.comments += 1
        instance.parent.save()

@receiver(post_delete, sender=QuestionComment)
def rem_ques_comment_count_from_question(instance, **kwargs):
    instance.parent.comments -= 1
    instance.parent.save()
# # # --------------------------------------------------- # # #

# # # ADD AND REMOVE ANSWER COMMENT COUNT IN THE ANSWER MODEL # # #
@receiver(post_save, sender=AnswerComment)
def add_ans_comment_count_to_answer(instance, created, **kwargs):
    if created:
        instance.parent.comments += 1
        instance.parent.save()

@receiver(post_delete, sender=AnswerComment)
def rem_ans_comment_count_from_answer(instance, **kwargs):
    instance.parent.comments -= 1
    instance.parent.save()
# # # --------------------------------------------------- # # #

# # # ADD AND REMOVE QUESTION HEARTS COUNT IN THE QUESTION MODEL # # #
@receiver(post_save, sender=QuestionHeart)
def add_ques_heart_count_to_question(instance, created, **kwargs):
    if created:
        instance.question.hearts += 1
        instance.question.save()

@receiver(post_delete, sender=QuestionHeart)
def rem_ques_heart_count_from_question(instance, **kwargs):
    instance.question.hearts -= 1
    instance.question.save()
# # # --------------------------------------------------- # # #

# # # ADD AND REMOVE QUESTION FLAGS COUNT IN THE QUESTION MODEL # # #
@receiver(post_save, sender=QuestionFlag)
def add_ques_flag_count_to_question(instance, created, **kwargs):
    if created:
        instance.question.flags += 1
        instance.question.save()

@receiver(post_delete, sender=QuestionFlag)
def rem_ques_flag_count_from_question(instance, **kwargs):
    instance.question.flags -= 1
    instance.question.save()
# # # --------------------------------------------------- # # #

# # # ADD AND REMOVE ANSWER HEARTS COUNT IN THE ANSWER MODEL # # #
@receiver(post_save, sender=AnswerHeart)
def add_ans_heart_count_to_answer(instance, created, **kwargs):
    if created:
        instance.answer.hearts += 1
        instance.answer.save()

@receiver(post_delete, sender=AnswerHeart)
def rem_ans_heart_count_from_answer(instance, **kwargs):
    instance.answer.hearts -= 1
    instance.answer.save()
# # # --------------------------------------------------- # # #

# # # ADD AND REMOVE ANSWER FLAGS COUNT IN THE ANSWER MODEL # # #
@receiver(post_save, sender=AnswerFlag)
def add_ans_flag_count_to_answer(instance, created, **kwargs):
    if created:
        instance.answer.flags += 1
        instance.answer.save()

@receiver(post_delete, sender=AnswerFlag)
def rem_ans_flag_count_from_answer(instance, **kwargs):
    instance.answer.flags -= 1
    instance.answer.save()
# # # --------------------------------------------------- # # #


# # # ADD AND REMOVE QUESTION COMMENT HEARTS COUNT IN THE QUESTION COMMENT MODEL # # #
@receiver(post_save, sender=QuestionCommentHeart)
def add_ques_comment_heart_count_to_question_comment(instance, created, **kwargs):
    if created:
        instance.comment.hearts += 1
        instance.comment.save()

@receiver(post_delete, sender=QuestionCommentHeart)
def rem_ques_comment_heart_count_from_question_comment(instance, **kwargs):
    instance.comment.hearts -= 1
    instance.comment.save()
# # # --------------------------------------------------- # # #

# # # ADD AND REMOVE QUESTION COMMENT FLAGS COUNT IN THE QUESTION COMMENT MODEL # # #
@receiver(post_save, sender=QuestionCommentFlag)
def add_ques_comment_flag_count_to_question_comment(instance, created, **kwargs):
    if created:
        instance.comment.flags += 1
        instance.comment.save()

@receiver(post_delete, sender=QuestionCommentFlag)
def rem_ques_comment_flag_count_from_question_comment(instance, **kwargs):
    instance.comment.flags -= 1
    instance.comment.save()
# # # --------------------------------------------------- # # #

# # # ADD AND REMOVE ANSWER COMMENT HEARTS COUNT IN THE ANSWER COMMENT MODEL # # #
@receiver(post_save, sender=AnswerCommentHeart)
def add_ans_comment_heart_count_to_answer_comment(instance, created, **kwargs):
    if created:
        instance.comment.hearts += 1
        instance.comment.save()

@receiver(post_delete, sender=AnswerCommentHeart)
def rem_ans_comment_heart_count_from_answer_comment(instance, **kwargs):
    instance.comment.hearts -= 1
    instance.comment.save()
# # # --------------------------------------------------- # # #

# # # ADD AND REMOVE ANSWER COMMENT FLAGS COUNT IN THE ANSWER COMMENT MODEL # # #
@receiver(post_save, sender=AnswerCommentFlag)
def add_ans_comment_flag_count_to_answer_comment(instance, created, **kwargs):
    if created:
        instance.comment.flags += 1
        instance.comment.save()

@receiver(post_delete, sender=AnswerCommentFlag)
def rem_ans_comment_flag_count_from_answer_comment(instance, **kwargs):
    instance.comment.flags -= 1
    instance.comment.save()
# # # --------------------------------------------------- # # #

# this has to be atomic transaction
@receiver(post_save, sender=Answer)
def answer_written_notification_to_questioner(instance, created, **kwargs):
    if created:
        actor = instance.author
        action = 'wrote an answer to your question.'
        user = instance.parent.author
        url = '/question/%s/' % instance.parent.id

        obj, created = NotificationObject.objects.update_or_create(user=user, action=action, url=url, is_read=False, defaults={
            "primary_actor": actor.username,
        })

        NotificationObjectActor.objects.create(obj=obj, actor=actor)

# this function is need for the above function to work
@receiver(pre_save, sender=NotificationObjectActor)
def increase_actor_count_in_notification_object(sender, instance, **kwargs):
    already_present = sender.objects.filter(obj=instance.obj, actor=instance.actor)
    if not already_present:
        instance.obj.actor_count += 1
        instance.obj.save()


@receiver(post_save, sender=QuestionComment)
def comment_written_notification_to_questioner(instance, created, **kwargs):
    if created:
        actor = instance.author
        action = 'commented on your question.'
        user = instance.parent.author
        url = '/question/%s/' % instance.parent.id

        obj, created = NotificationObject.objects.update_or_create(user=user, action=action, url=url, is_read=False, defaults={
            "primary_actor": actor.username,
        })

        NotificationObjectActor.objects.create(obj=obj, actor=actor)

@receiver(post_save, sender=AnswerComment)
def comment_written_notification_to_answerer(instance, created, **kwargs):
    if created:
        actor = instance.author
        action = 'commented on your answer.'
        user = instance.parent.author
        url = '/answer/%s/' % instance.parent.id

        obj, created = NotificationObject.objects.update_or_create(user=user, action=action, url=url, is_read=False, defaults={
            "primary_actor": actor.username,
        })

        NotificationObjectActor.objects.create(obj=obj, actor=actor)

@receiver(post_save, sender=QuestionHeart)
def question_heart_notification_to_questioner(instance, created, **kwargs):
    if created:
        actor = instance.user
        action = 'hearted your question.'
        user = instance.question.author
        url = '/question/%s/' % instance.id

        obj, created = NotificationObject.objects.update_or_create(user=user, action=action, url=url, is_read=False, defaults={
            "primary_actor": actor.username,
        })

        NotificationObjectActor.objects.create(obj=obj, actor=actor)

# Make a handler for deleting notification when user unhearts question

@receiver(post_save, sender=AnswerHeart)
def answer_heart_notification_to_answerer(instance, created, **kwargs):
    if created:
        actor = instance.user
        action = 'hearted <a href="/question/' + str(instance.answer.parent.id) +  '/">your answer</a>.'
        user = instance.answer.parent.author
        url = '/answer/%s/' % instance.id

        obj, created = NotificationObject.objects.update_or_create(user=user, action=action, url=url, is_read=False, defaults={
            "primary_actor": actor.username,
        })

        NotificationObjectActor.objects.create(obj=obj, actor=actor)

# Make a handler for deleting notification when user unhearts answer

