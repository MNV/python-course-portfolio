from django.urls import path

from jobs.views import IndexJobsDetailView

urlpatterns = [
    path("<int:pk>/", IndexJobsDetailView.as_view(), name="job"),
]