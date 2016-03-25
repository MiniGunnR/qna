from django.shortcuts import render
from django.http import JsonResponse

from .models.models import Question, QuestionFlag, QuestionHeart, QuestionCommentHeart, QuestionCommentFlag,\
    Answer, AnswerFlag, AnswerHeart, AnswerCommentHeart, AnswerCommentFlag

def QuestionHeartView(request, pk):
    obj, created = QuestionHeart.objects.get_or_create(question_id=pk, user=request.user)

    if not created:
        obj.delete()
        return JsonResponse({"response": "unhearted"})
    else:
        return JsonResponse({"response": "hearted"})

def AnswerHeartView(request, pk):
    obj, created = AnswerHeart.objects.get_or_create(answer_id=pk, user=request.user)

    if not created:
        obj.delete()
        return JsonResponse({"response": "unhearted"})
    else:
        return JsonResponse({"response": "hearted"})

def QuestionFlagView(request, pk):
    obj, created = QuestionFlag.objects.get_or_create(question_id=pk, user=request.user)

    if not created:
        obj.delete()
        return JsonResponse({"response": "unflagged"})
    else:
        return JsonResponse({"response": "flagged"})

def AnswerFlagView(request, pk):
    obj, created = AnswerFlag.objects.get_or_create(answer_id=pk, user=request.user)

    if not created:
        obj.delete()
        return JsonResponse({"response": "unflagged"})
    else:
        return JsonResponse({"response": "flagged"})

def QuestionCommentHeartView(request, pk):
    obj, created = QuestionCommentHeart.objects.get_or_create(comment_id=pk, user=request.user)

    if not created:
        obj.delete()
        return JsonResponse({"response": "unhearted"})
    else:
        return JsonResponse({"response": "hearted"})

def AnswerCommentHeartView(request, pk):
    obj, created = AnswerCommentHeart.objects.get_or_create(comment_id=pk, user=request.user)

    if not created:
        obj.delete()
        return JsonResponse({"response": "unhearted"})
    else:
        return JsonResponse({"response": "hearted"})

def QuestionCommentFlagView(request, pk):
    obj, created = QuestionCommentFlag.objects.get_or_create(comment_id=pk, user=request.user)

    if not created:
        obj.delete()
        return JsonResponse({"response": "unflagged"})
    else:
        return JsonResponse({"response": "flagged"})

def AnswerCommentFlagView(request, pk):
    obj, created = AnswerCommentFlag.objects.get_or_create(comment_id=pk, user=request.user)

    if not created:
        obj.delete()
        return JsonResponse({"response": "unflagged"})
    else:
        return JsonResponse({"response": "flagged"})
