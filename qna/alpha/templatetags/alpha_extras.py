from django import template

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
