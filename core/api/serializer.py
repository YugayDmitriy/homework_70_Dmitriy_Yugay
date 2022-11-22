from rest_framework import serializers
from issuetracker.models import Issue, Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'start_date', 'end_date')
        read_only_fields = ('start_date', 'end_date')


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'summary', 'description', 'status', 'type', 'project')
        read_only_fields = ('id', 'summary', 'project')
