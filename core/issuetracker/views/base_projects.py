from django.utils.http import urlencode
from django.views.generic import ListView
from django.db.models import Q
from urllib.parse import urlencode
from issuetracker.models import Project
from issuetracker.forms import SearchForm


class IndexProjectView(ListView):
    template_name = "index_projects.html"
    model = Project
    context_object_name = 'projects'
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

    def get_queryset(self):
        queryset = super().get_queryset().all()
        if self.search_value:
            query = Q(name__icontains=self.search_value) | Q(name__icontains=self.search_value)
            print(query.__dict__)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexProjectView, self).get_context_data(object_list=object_list, **kwargs)
        context.update({'projects': Project.objects.filter(is_deleted=False)})
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context
