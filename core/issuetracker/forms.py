from django import forms
from django.core.exceptions import ValidationError
from django.forms import Textarea
from issuetracker.models import Issue
from issuetracker.models import Type
from issuetracker.models import Status
from issuetracker.models import Project


# class SummaryLengthValidator(BaseValidator):
#     def __init__(self, limit_value=40):
#         message = 'Максимальное значение символ (а/ов) %(limit_value)s. Вы ввели %(show_value)s символ (а/ов)'
#         super(SummaryLengthValidator, self).__init__(limit_value=limit_value, message=message)
#
#     def compare(self, value, max_value):
#         return max_value < value
#
#     def clean(self, value):
#         return len(value)


class IssueForm(forms.ModelForm):
    summary = forms.CharField(
        label='Задача',
        max_length=300,
        )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        empty_label='Статус не выбран'),
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


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')

    class Meta:
        model = Issue
        fields = "search"
        widgets = {
            'search': Textarea(attrs={'class': 'form-control mr-sm-2'})
        }


class ProjectForm(forms.ModelForm):
    name = forms.CharField(
        label='Название проекта'
    )
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea
    )
    start_date = forms.DateField(
        label='Дата начала',
        widget=forms.SelectDateWidget
    )
    end_date = forms.DateField(
        label='Дата окончания',
        widget=forms.SelectDateWidget
    )

    class Meta:
        model = Project
        fields = ('name', 'description', 'start_date', 'end_date')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 21, 'rows': 5}),
            }
