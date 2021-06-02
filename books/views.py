from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
from django.views.generic import ListView, DetailView
from .models import Book
from django.db.models import Q

class BookListView(ListView, LoginRequiredMixin): 
  model = Book
  context_object_name = 'book_list'
  template_name = 'books/book_list.html'
  login_url = 'account_login'


class BookDetailView(DetailView, PermissionRequiredMixin):
  model = Book
  context_object_name = 'book'
  template_name = 'books/book_detail.html'
  login_url = 'account_login'
  permission_required = 'book.read_all_books'

class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):
      query = self.request.GET.get('q') 
      return Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query)
      )
