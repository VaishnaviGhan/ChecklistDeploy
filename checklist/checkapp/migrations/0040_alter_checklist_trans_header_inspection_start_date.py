# Generated by Django 4.1.7 on 2023-09-08 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0039_alter_checklist_trans_header_project_head_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist_trans_header',
            name='inspection_Start_Date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
