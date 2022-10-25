from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import DeleteView
from issuetracker.models import Issue


class IssueDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'delete_confirm.html'
    model = Issue
    success_message = "Задача %(summary)s успешно удалена"

    def get_success_url(self):
        return reverse('index')
