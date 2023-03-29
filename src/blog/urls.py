from django.urls import path

from blog.views import BlogsListView
from blog.views import BlogsDetailView

urlpatterns = [
    path("", BlogsListView.as_view(), name="blogs"),
    path("<int:pk>/", BlogsDetailView.as_view(), name="blog"),
]
