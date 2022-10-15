from django import forms
from django.core.exceptions import ValidationError
from issuetracker.models import Issue
from issuetracker.models import Type
from issuetracker.models import Status


class IssueForm(forms.ModelForm):

    status = forms.ModelChoiceField(queryset=Status.objects.all(), empty_label='Статус не выбран')
    type = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Issue
        fields = ('summary', 'description', 'status', 'type')

    def clean_title(self):
        summary = self.cleaned_data.get('summary')
        if Issue.objects.filter(summary=summary).exists():
            raise ValidationError('Запись с таким заголовком уже существует')
        return summary
