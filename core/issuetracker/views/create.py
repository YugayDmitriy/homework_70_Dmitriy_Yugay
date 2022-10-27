from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import CreateView
from issuetracker.forms import IssueForm
from issuetracker.models import Issue


class IssueAddView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    form_class = IssueForm
    model = Issue
    success_message = "Задача %(summary)s успешно добавлена"

    def form_valid(self, form):
        form.instance.project_id = self.kwargs['pk']
        return super(IssueAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse('index')
