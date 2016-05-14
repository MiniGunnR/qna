from django.shortcuts import render
from django.http import JsonResponse
from itertools import chain
from operator import attrgetter
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import requests

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models.models import Question, QuestionFlag, QuestionHeart, QuestionCommentHeart, QuestionCommentFlag,\
    Answer, AnswerFlag, AnswerHeart, AnswerCommentHeart, AnswerCommentFlag, QuestionComment, AnswerComment

from .serializers import QuestionCommentSerializer, AnswerCommentSerializer, AnswerSerializer

from rest_framework import generics


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

@login_required()
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
    comments = QuestionComment.objects.all()
    return render(request, "alpha/stream.html", {'queryset': queryset, 'comments': comments})


class StreamAPI(generics.ListAPIView):
    model = 


class QuestionDetail(DetailView):
    model = Question
    template_name = 'alpha/question-detail.html'

    def get_context_data(self, **kwargs):
        context = super(QuestionDetail, self).get_context_data(**kwargs)
        context['answers'] = Answer.objects.filter(parent=self.object)
        return context


class AnswerDetail(DetailView):
    model = Answer
    template_name = 'alpha/answer-detail.html'


class QuestionCreate(CreateView):
    model = Question
    fields = ['title', 'body', 'category']
    template_name = 'alpha/question-create.html'

    def get_success_url(self):
        return reverse('question-detail', args=(self.object.id,))

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(QuestionCreate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


def LoginView(request):
    next = request.GET.get('next', '/stream/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "alpha/login.html", {'redirect_to': next})


def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)


class QuestionCommentList(generics.ListCreateAPIView):
    serializer_class = QuestionCommentSerializer

    def get_queryset(self):
        return QuestionComment.objects.filter(parent=self.kwargs['pk']).order_by('-created')


class AnswerCommentList(generics.ListCreateAPIView):
    serializer_class = AnswerCommentSerializer

    def get_queryset(self):
        return AnswerComment.objects.filter(parent=self.kwargs['pk']).order_by('-created')


def HtmlQuestionComment(request, pk):
    url = requests.get("http://127.0.0.1:8000/show/ques/%s/comments/" % pk)
    json_string = url.json()
    return render(request, "alpha/html-ques-comments.html", {'comments': json_string, 'pk': pk})


def HtmlAnswerComment(request, pk):
    url = requests.get("http://127.0.0.1:8000/show/ans/%s/comments/" % pk)
    json_string = url.json()
    return render(request, "alpha/html-ans-comments.html", {'comments': json_string, 'pk': pk})


def HtmlQuestionCommentForm(request, pk):
    return render(request, "alpha/html-ques-comment-form.html", {"pk": pk})


class AnswerView(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return Answer.objects.filter(parent=self.kwargs['pk']).order_by('-created')


def AnswerForm(request, pk):
    return render(request, "alpha/ans-form.html", {"pk": pk})
