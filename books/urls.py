from django.urls import include, path
from rest_framework import routers

from .views import BookDetailView, BookListView, BookViewSet, SearchResultsListView

router = routers.DefaultRouter()
router.register(r"books", BookViewSet)

urlpatterns = [
    path("api", include(router.urls)),
    path("", BookListView.as_view(), name="book_list"),
    path("<uuid:pk>", BookDetailView.as_view(), name="book_detail"),
    path("search", SearchResultsListView.as_view(), name="search_results"),
]
