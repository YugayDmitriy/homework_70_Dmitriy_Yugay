from django.urls import reverse
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from issuetracker.forms import ProjectForm
from issuetracker.models import Project, Issue


class ProjectDetailView(DetailView):
    template_name = 'project_detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        issue = project.issue.order_by('-created_at')
        context['issue_list'] = issue
        return context


class ProjectAddView(SuccessMessageMixin, CreateView):
    template_name = 'create_project.html'
    form_class = ProjectForm
    model = Project
    success_message = "Проект %(name)s успешно добавлен"

    def get_success_url(self):
        return reverse('index_projects')


class ProjectEditView(SuccessMessageMixin, UpdateView):
    template_name = 'edit_project.html'
    form_class = ProjectForm
    model = Project
    success_message = "Проект %(name)s успешно отредактирован"

    def get_success_url(self):
        return reverse('index_projects')


class ProjectDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'confirm_delete_project.html'
    model = Project
    success_message = "Проект %(summary)s успешно удален"

    def get_success_url(self):
        return reverse('detail_project', kwargs={'pk': self.object.pk})
