from django.urls import path
from .views.base_projects import IndexProjectView
from .views.create import IssueAddView
from .views.base import IndexView
from .views.delete import IssueDeleteView
from .views.details import IssueDetailView
from .views.edit import IssueEditView
from .views.projects import ProjectAddView, ProjectEditView, ProjectDeleteView, ProjectDetailView

urlpatterns = [
   path("", IndexProjectView.as_view(), name='index_projects'),
   path("issue_list", IndexView.as_view(), name='index'),
   path('add_project', ProjectAddView.as_view(), name='add_project'),
   path('projects/<int:pk>/add_issue/', IssueAddView.as_view(), name='add_issue'),
   path('edit_project/<int:pk>', ProjectEditView.as_view(), name='edit_project'),
   path('edit_issue/<int:pk>', IssueEditView.as_view(), name='edit_issue'),
   path('detail_project/<int:pk>', ProjectDetailView.as_view(), name='detail_project'),
   path('detail_issue/<int:pk>', IssueDetailView.as_view(), name='detail_issue'),
   path('delete_project/<int:pk>', ProjectDeleteView.as_view(), name='delete_project'),
   path('delete_issue/<int:pk>', IssueDeleteView.as_view(), name='delete_issue'),
]

