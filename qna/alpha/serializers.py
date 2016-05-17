from rest_framework import serializers

from models.models import QuestionComment, AnswerComment, Answer, Question

class QuestionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionComment
        fields = ('id', 'parent', 'author', 'body')


class AnswerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerComment
        fields = ('id', 'parent', 'author', 'body')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'parent', 'author', 'body', 'comments')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'author', 'body', 'comments')


