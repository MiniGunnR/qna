from django.contrib import admin

from models.models import Question, Answer, QuestionComment, AnswerComment, Category, \
    QuestionHeart, QuestionFlag, AnswerHeart, AnswerFlag, QuestionCommentHeart, QuestionCommentFlag, AnswerCommentHeart, \
    AnswerCommentFlag, Notification, QuestionFollowers


admin.site.register(Category)

class QuestionAdmin(admin.ModelAdmin):
    fields = ('category', 'title', 'body', 'author', 'anonymous', 'hearts', 'flags', 'answers', 'comments', 'closed')
admin.site.register(Question, QuestionAdmin)

class QuestionCommentAdmin(admin.ModelAdmin):
    fields = ('parent', 'body', 'author', 'anonymous', 'hearts', 'flags')
admin.site.register(QuestionComment, QuestionCommentAdmin)

class AnswerAdmin(admin.ModelAdmin):
    fields = ('parent', 'body', 'author', 'anonymous', 'hearts', 'flags', 'comments')
admin.site.register(Answer, AnswerAdmin)

class AnswerCommentAdmin(admin.ModelAdmin):
    fields = ('parent', 'body', 'author', 'anonymous', 'hearts', 'flags')
admin.site.register(AnswerComment, AnswerCommentAdmin)

admin.site.register(QuestionHeart)
admin.site.register(QuestionFlag)
admin.site.register(AnswerHeart)
admin.site.register(AnswerFlag)
admin.site.register(QuestionCommentHeart)
admin.site.register(QuestionCommentFlag)
admin.site.register(AnswerCommentHeart)
admin.site.register(AnswerCommentFlag)
admin.site.register(Notification)
admin.site.register(QuestionFollowers)
