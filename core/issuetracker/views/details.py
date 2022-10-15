from django.shortcuts import get_object_or_404
from issuetracker.models import Issue
from django.views.generic import TemplateView


class IssueDetailView(TemplateView):
    template_name = 'issue_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue_detail'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context
