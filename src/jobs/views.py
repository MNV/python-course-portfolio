from django.views.generic import ListView, DetailView

from jobs.models import Job


class IndexJobsListView(ListView):
    model = Job


class JobDetailView(DetailView):
    model = Job
