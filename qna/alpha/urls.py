from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^heart/question/(?P<pk>\d+)/$', views.QuestionHeartView, name='question-heart'),
    url(r'^heart/answer/(?P<pk>\d+)/$', views.AnswerHeartView, name='answer-heart'),

    url(r'^flag/question/(?P<pk>\d+)/$', views.QuestionFlagView, name='question-flag'),
    url(r'^flag/answer/(?P<pk>\d+)/$', views.AnswerFlagView, name='answer-flag'),

    url(r'^heart/question/comment/(?P<pk>\d+)/$', views.QuestionCommentHeartView, name='question-comment-heart'),
    url(r'^heart/answer/comment/(?P<pk>\d+)/$', views.AnswerCommentHeartView, name='answer-comment-heart'),

    url(r'^flag/question/comment/(?P<pk>\d+)/$', views.QuestionCommentFlagView, name='question-comment-flag'),
    url(r'^flag/answer/comment/(?P<pk>\d+)/$', views.AnswerCommentFlagView, name='answer-comment-flag'),

    url(r'^login/$', views.LoginView, name='login'),
    url(r'^logout/$', views.LogoutView, name='logout'),

    url(r'^stream/$', views.Stream, name='stream'),
    # url(r'^api/stream/$', views.StreamAPI, name='stream-api'),

    url(r'^question/(?P<pk>\d+)/$', views.QuestionDetail.as_view(), name='question-detail'),
    url(r'^answer/(?P<pk>\d+)/$', views.AnswerDetail.as_view(), name='answer-detail'),

    url(r'^ask/$', views.QuestionCreate.as_view(), name='question-create'),

    url(r'^show/ques/(?P<pk>\d+)/comments/$', views.QuestionCommentList.as_view(), name='show-ques-comments'),
    url(r'^show/ans/(?P<pk>\d+)/comments/$', views.AnswerCommentList.as_view(), name='show-ans-comments'),

    url(r'^html/ques/(?P<pk>\d+)/comments/$', views.HtmlQuestionComment, name='html-ques-comments'),
    url(r'^html/ans/(?P<pk>\d+)/comments/$', views.HtmlAnswerComment, name='html-ans-comments'),

    url(r'^html/ques/(?P<pk>\d+)/comment/form/$', views.HtmlQuestionCommentForm, name='html-ques-comment-form'),
    url(r'^html/ans/(?P<pk>\d+)/comment/form/$', views.HtmlAnswerCommentForm, name='html-ans-comment-form'),

    url(r'^api/ques/(?P<pk>\d+)/answer/$', views.AnswerView.as_view(), name='answer-view'),

    url(r'^html/ques/(?P<pk>\d+)/answer/$', views.AnswerForm, name='answer-form'),
    url(r'^html/ques/(?P<pk>\d+)/answer/in/detail/page/$', views.AnswerFormDetail, name='answer-form-detail'),

    url(r'^notifications/$', views.Notifications, name='notifications'),

    url(r'^follow/question/(?P<pk>\d+)/$', views.QuestionFollowView, name='question-follow'),

    url(r'^search/$', views.Search, name='search'),
]
