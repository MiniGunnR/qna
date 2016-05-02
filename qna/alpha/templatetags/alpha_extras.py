from django import template
from django.contrib.auth.models import User

from ..models.models import QuestionHeart, AnswerHeart

register = template.Library()


@register.filter
def check_ans_heart(value, arg):
    try:
        obj = AnswerHeart.objects.get(answer_id=value, user=arg)
    except:
        return False
    else:
        return True


@register.filter
def check_ques_heart(value, arg):
    try:
        obj = QuestionHeart.objects.get(question_id=value, user=arg)
    except:
        return False
    else:
        return True


@register.filter
def get_username(value):
    try:
        obj = User.objects.get(id=value)
    except:
        return value
    else:
        return obj.username
