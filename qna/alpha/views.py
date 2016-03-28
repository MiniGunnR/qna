from django.shortcuts import render
from django.http import JsonResponse
from itertools import chain
from operator import attrgetter

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

# # #

def Stream(request):
    questions = Question.objects.all()
    answers = Answer.objects.all()
    combined = sorted(chain(questions, answers), key=attrgetter('created'), reverse=True)
    queryset = []
    for item in combined:
        if hasattr(item, 'parent'):
            try:
                qs = AnswerHeart.objects.get(answer=item, user=request.user)
                if qs:
                    point = True
            except AnswerHeart.DoesNotExist:
                point = False
            queryset.append((item, point))
        else:
            try:
                qs = QuestionHeart.objects.get(question=item, user=request.user)
                if qs:
                    point = True
            except QuestionHeart.DoesNotExist:
                point = False
            queryset.append((item, point))
    return render(request, "alpha/stream.html", {'queryset': queryset})
