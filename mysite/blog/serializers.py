from django import forms
from rest_framework import serializers

from blog.models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'demo_content']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'created_at']

# class CommentSerializer(serializers.ModelSerializer):
#
#         class Meta:
#             model = Comment
#             fields = ['title']
