from django.urls import path
from api.views import ProjectListView, ProjectDetailView, ProjectUpdateView, ProjectDeleteView, IssueListView, \
    IssueDetailView, IssueUpdateView, IssueDeleteView

urlpatterns = [
    path('project/detail/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('project/update/<int:pk>', ProjectUpdateView.as_view(), name='project_update'),
    path('project/delete/<int:pk>', ProjectDeleteView.as_view(), name='project_delete'),
    path('issue/detail/<int:pk>', IssueDetailView.as_view(), name='issue_detail'),
    path('issue/update/<int:pk>', IssueUpdateView.as_view(), name='issue_update'),
    path('issue/delete/<int:pk>', IssueDeleteView.as_view(), name='issue_delete'),
]
