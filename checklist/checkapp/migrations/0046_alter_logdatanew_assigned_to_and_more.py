# Generated by Django 4.1.7 on 2023-09-12 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0045_logdatanew_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logdatanew',
            name='assigned_to',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='logdatanew',
            name='assigned_to_ProjectHead',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='logdatanew',
            name='assigned_to_ProjectQA',
            field=models.CharField(max_length=100, null=True),
        ),
    ]