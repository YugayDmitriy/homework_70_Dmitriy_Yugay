from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from issuetracker.forms import IssueForm


class IssueAddView(TemplateView):
    template_name = 'create.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = IssueForm()
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save()
            messages.info(request, 'Задача успешно добавлена')
            return redirect('index', pk=issue.pk)
        return render(request, 'create.html', context={'form': form})
