from django.urls import path

from jobs.views import IndexJobsListView
from jobs.views import JobDetailView

urlpatterns = [
    path("", IndexJobsListView.as_view(), name="jobs"),
    path("<int:pk>/", JobDetailView.as_view(), name="job"),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]