from django.urls import reverse
from django.views.generic import UpdateView
from issuetracker.forms import IssueForm
from issuetracker.models import Issue
from django.contrib.messages.views import SuccessMessageMixin


class IssueEditView(SuccessMessageMixin, UpdateView):
    template_name = 'edit.html'
    form_class = IssueForm
    model = Issue
    success_message = "Задача %(summary)s успешно отредактирована"

    def get_success_url(self):
        return reverse('index')
