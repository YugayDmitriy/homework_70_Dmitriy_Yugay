from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView
from issuetracker.forms import IssueForm
from issuetracker.models import Issue


class IssueEditView(TemplateView):
    template_name = 'edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue_edit'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = IssueForm(instance=context['issue_edit'])
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        todo_issue = get_object_or_404(Issue, pk=kwargs['pk'])
        form = IssueForm(request.POST, instance=todo_issue)
        if form.is_valid():
            form.save()
            messages.info(request, "Задача успешно отредактирована")
            return redirect('index')
        return render(request, 'edit.html', context={'form': form})
