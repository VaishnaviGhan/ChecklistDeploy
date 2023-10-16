# Generated by Django 4.1.7 on 2023-09-07 04:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0036_checklist_footer_initial_checks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist_trans_header',
            name='assigned_to_is_DHEQA',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assigned_to_is_DHEQA', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='checklist_trans_header',
            name='assigned_to_is_ProjectHead',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assigned_to_is_ProjectHead', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='checklist_trans_header',
            name='assigned_to_is_ProjectQA',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assigned_to_is_ProjectQA', to=settings.AUTH_USER_MODEL),
        ),
    ]