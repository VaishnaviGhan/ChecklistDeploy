# Generated by Django 4.1.7 on 2023-07-18 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0011_checklist_trans_header_chainage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist_trans_details',
            name='CheckList_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkapp.checklist_header'),
        ),
    ]
