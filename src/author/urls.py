from django.urls import path

from author.views import AutorListView
from author.views import AutorDetailView

urlpatterns = [
    path("", AutorListView.as_view(), name="authors"),
    path("<int:pk>/", AutorDetailView.as_view(), name="author"),
]
