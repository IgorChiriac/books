from rest_framework import serializers

from books.models import Book
from users.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "cover", "created_at", "updated_at")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["url", "username", "email", "groups"]
