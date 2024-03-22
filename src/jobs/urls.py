from django.urls import path
from jobs.views import IndexJobDetailedView


urlpatterns = [
    path("<int:pk>/",
         IndexJobDetailedView.as_view(),
         name="job"),
]
