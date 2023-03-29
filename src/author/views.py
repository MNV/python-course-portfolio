from django.views.generic import ListView
from django.views.generic import DetailView

from author.models import Author


class AuthorListView(ListView):
    model = Author


class AuthorDetailView(DetailView):
    model = Author
