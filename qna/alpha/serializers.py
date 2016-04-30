from rest_framework import serializers

from models.models import QuestionComment, AnswerComment

class QuestionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionComment
        fields = ('author', 'body')

class AnswerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerComment
        fields = ("author", "body")
