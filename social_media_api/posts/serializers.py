from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # Read-only author field

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # Read-only author field
    post_title = serializers.ReadOnlyField(source='post.title')  # Include the post title for context

    class Meta:
        model = Comment
        fields = ['id', 'post', 'post_title', 'author', 'content', 'created_at', 'updated_at']

