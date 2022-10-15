from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView
from issuetracker.models import Issue


class IssueDeleteView(TemplateView):
    template_name = 'delete_confirm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue_delete'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        issue_delete = get_object_or_404(Issue, pk=kwargs['pk'])
        issue_delete.delete()
        messages.info(request, "Задача успешно удалена")
        return redirect('index')
