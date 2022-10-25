from django.contrib import admin
from issuetracker.models import Issue
from issuetracker.models import Type
from issuetracker.models import Status
from issuetracker.models import Project


class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'description', 'status', 'created_at', 'updated_at')
    list_filter = ('id', 'summary', 'description', 'type', 'status', 'created_at', 'updated_at')
    search_fields = ('summary', 'description', 'type', 'status')
    fields = ('summary', 'description', 'type', 'status', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Issue, IssueAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_filter = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')
    fields = ('name', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Status)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_filter = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')
    fields = ('name', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Type)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'start_date', 'end_date')
    list_filter = ('id', 'name', 'description', 'start_date', 'end_date')
    search_fields = ('name', 'description')
    fields = ('name', 'description', 'start_date', 'end_date')
    readonly_fields = ('id', 'start_date', 'end_date')


admin.site.register(Project)
