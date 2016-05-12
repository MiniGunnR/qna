from rest_framework import serializers

from models.models import QuestionComment, AnswerComment, Answer

class QuestionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionComment
        fields = ('parent', 'author', 'body')


class AnswerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerComment
        fields = ('parent', 'author', 'body')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('parent', 'author', 'body', 'comments')
