# Generated by Django 4.1.7 on 2023-09-08 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0041_checklist_trans_header_assigned_to_projecthead_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist_trans_header',
            old_name='assigned_to_ProjectHead',
            new_name='submit_to_ProjectHead',
        ),
        migrations.RenameField(
            model_name='checklist_trans_header',
            old_name='assigned_to_ProjectQA',
            new_name='submit_to_ProjectQA',
        ),
    ]
