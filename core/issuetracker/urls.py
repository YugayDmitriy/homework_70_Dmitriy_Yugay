from django.urls import path
from .views.create import IssueAddView
from .views.base import IndexView
from .views.delete import IssueDeleteView
from .views.details import IssueDetailView
from .views.edit import IssueEditView

urlpatterns = [
   path("", IndexView.as_view(), name='index'),
   path('add_issue', IssueAddView.as_view(), name='add_issue'),
   path('edit_issue/<int:pk>', IssueEditView.as_view(), name='edit_issue'),
   path('detail_issue/<int:pk>', IssueDetailView.as_view(), name='detail_issue'),
   path('delete_issue/<int:pk>', IssueDeleteView.as_view(), name='delete_issue'),
]

