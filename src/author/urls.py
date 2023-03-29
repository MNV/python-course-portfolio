from django.urls import path

from author.views import AuthorListView
from author.views import AuthorDetailView

urlpatterns = [
    path("", AuthorListView.as_view(), name="authors"),
    path("<int:pk>/", AuthorDetailView.as_view(), name="author"),
]
