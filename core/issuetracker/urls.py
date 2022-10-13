from django.urls import path

from .views.base import IndexView

urlpatterns = [
   path("", IndexView.as_view(), name='index'),
]