from rest_framework import serializers

from users.serializers import ProfileSerializer
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'profile', 'post', 'text')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'text')


# 같은 Post 모델에 대해서 두가지 시리얼라이저 (왜냐하면 용도가 다름)
class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True) # profile 필드에 profile의 pk 값만 나타나지 않도록 함. 작성자 프로필을 알 수 있게 =>  nested serializer
    comments = CommentSerializer(many=True, read_only=True) # 댓글 시리얼라이저를 포함하여 댓글 추가, many=True를 통해 다수의 댓글 포함.

    class Meta:
        model = Post
        fields = ('pk', 'profile', 'title', 'body', 'image', 'published_date', 'likes', 'comments')


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "category", "body", "image")