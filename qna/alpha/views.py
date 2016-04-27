from django.shortcuts import render
from django.http import JsonResponse
from itertools import chain
from operator import attrgetter

from django.views.generic.detail import DetailView

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
                qs_heart = AnswerHeart.objects.get(answer=item, user=request.user)
                if qs_heart:
                    hearted = True
            except AnswerHeart.DoesNotExist:
                hearted = False
            try:
                qs_flag = AnswerFlag.objects.get(answer=item, user=request.user)
                if qs_flag:
                    flagged = True
            except AnswerFlag.DoesNotExist:
                flagged = False
            queryset.append((item, hearted, flagged))
        else:
            try:
                qs_heart = QuestionHeart.objects.get(question=item, user=request.user)
                if qs_heart:
                    hearted = True
            except QuestionHeart.DoesNotExist:
                hearted = False
            try:
                qs_flag = QuestionFlag.objects.get(question=item, user=request.user)
                if qs_flag:
                    flagged = True
            except QuestionFlag.DoesNotExist:
                flagged = False
            queryset.append((item, hearted, flagged))
    return render(request, "alpha/stream.html", {'queryset': queryset})


class QuestionDetail(DetailView):
    model = Question
    template_name = 'alpha/question-detail.html'


class AnswerDetail(DetailView):
    model = Answer
    template_name = 'alpha/answer-detail.html'

