from rest_framework import permissions, viewsets

from books.api.serializers import BookSerializer
from books.models import Book


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """

    queryset = Book.objects.all().order_by("-updated_at")
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
