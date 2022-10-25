from issuetracker.models import Issue
from django.views.generic import DetailView


class IssueDetailView(DetailView):
    template_name = 'issue_detail.html'
    model = Issue
    context_object_name = 'issue_detail'
