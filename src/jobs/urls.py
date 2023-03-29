from django.urls import path

from jobs.views import IndexJobsListView
from jobs.views import JobsDetailView

urlpatterns = [
    path("", IndexJobsListView.as_view(), name="jobs"),
    path("<int:pk>/", JobsDetailView.as_view(), name="job"),
]
