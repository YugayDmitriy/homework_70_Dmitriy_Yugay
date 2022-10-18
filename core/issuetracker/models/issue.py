from django.db import models


class Issue(models.Model):
    summary = models.CharField(verbose_name='Задача', max_length=300)
    description = models.TextField(verbose_name='Описание', null=True, blank=True, max_length=1500)
    status = models.ForeignKey(
        to='issuetracker.Status',
        verbose_name='Статус',
        related_name='statuses',
        on_delete=models.PROTECT)
    type = models.ManyToManyField(
        to='issuetracker.Type',
        verbose_name='Тип',
        related_name='types',
        blank=True)
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Время изменения', auto_now=True)

    def __str__(self):
        return f"{self.summary} - {self.type} - {self.status}"
