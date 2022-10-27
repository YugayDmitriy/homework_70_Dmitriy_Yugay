# Generated by Django 3.2 on 2022-10-24 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issuetracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Наименование проекта')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(blank=True, default=None, verbose_name='Дата окончания')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(blank=True, max_length=1500, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='issue', to='issuetracker.status', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='summary',
            field=models.CharField(max_length=300, verbose_name='Задача'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='type',
            field=models.ManyToManyField(blank=True, related_name='issue', to='issuetracker.Type', verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='issue', to='issuetracker.project', verbose_name='Проект'),
        ),
    ]