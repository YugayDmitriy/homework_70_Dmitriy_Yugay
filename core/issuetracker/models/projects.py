from django.db import models
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(
        verbose_name='Наименование проекта',
        max_length=300,
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=1000,
        null=False,
        blank=False
    )
    start_date = models.DateField(
        verbose_name='Дата начала',
        null=False,
        blank=False
    )
    end_date = models.DateField(
        verbose_name='Дата окончания',
        null=False,
        blank=True,
        default=None
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False,
        null=False
    )

    def __str__(self):
        return f"{self.name} - {self.description}"

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
