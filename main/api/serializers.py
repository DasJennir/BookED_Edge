from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField,
)
from rest_framework import serializers
from main.models import Post
from django.utils import timezone


class PostCreateSerializer(ModelSerializer):

    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    date_posted = serializers.HiddenField(default=timezone.now)

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "schools",
            "course",
            "classes",
            "isbn",
            "semester",
            "visible",
            "date_posted",
        ]


class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "author",
            "title",
            "content",
            "schools",
            "course",
            "classes",
            "isbn",
            "semester",
            "visible",
        ]


class PostListSerializer(ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="Detail-API", lookup_field="pk"
    )
    author = SerializerMethodField()
    schools = SerializerMethodField()
    course = SerializerMethodField()
    classes = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "url",
            "title",
            "author",
            "schools",
            "course",
            "classes",
            "date_posted",
        ]

    def get_author(self, obj):
        return str(obj.author.username)

    def get_schools(self, obj):
        return str(obj.schools)

    def get_course(self, obj):
        return str(obj.course)

    def get_classes(self, obj):
        return str(obj.classes)


class PostDetailSerializer(ModelSerializer):
    author = SerializerMethodField()
    schools = SerializerMethodField()
    course = SerializerMethodField()
    classes = SerializerMethodField()
    post_img = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "content",
            "schools",
            "course",
            "classes",
            "isbn",
            "semester",
            "visible",
            "sponsored",
            "date_posted",
            "post_img",
        ]

    def get_author(self, obj):
        return str(obj.author.username)

    def get_schools(self, obj):
        return str(obj.schools)

    def get_course(self, obj):
        return str(obj.course)

    def get_classes(self, obj):
        return str(obj.classes)

    def get_post_img(self, obj):
        try:
            post_img = obj.image.path
        except:
            post_img = None
        return post_img