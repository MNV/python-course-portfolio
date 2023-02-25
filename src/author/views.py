from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView

from author.models import Author


class AuthorListView(ListView):
    model = Author


class AuthorDetailView(DetailView):
    model = Author
