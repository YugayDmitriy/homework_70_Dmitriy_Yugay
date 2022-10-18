from django.contrib import admin
from issuetracker.models import Issue
from issuetracker.models import Type
from issuetracker.models import Status


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


admin.site.register(Status, StatusAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_filter = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')
    fields = ('name', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Type, TypeAdmin)
