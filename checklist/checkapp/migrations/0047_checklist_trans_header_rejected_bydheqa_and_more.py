# Generated by Django 4.1.7 on 2023-09-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0046_alter_logdatanew_assigned_to_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist_trans_header',
            name='rejected_byDHEQA',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='checklist_trans_details',
            name='Site_Engineer_Status',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Na', 'NA'), ('Partial', 'Partial'), ('Not_Observed', 'Not_Observed')], default='Unspecified', max_length=70),
        ),
        migrations.AlterField(
            model_name='checklist_trans_header',
            name='Project_Head_Status',
            field=models.CharField(choices=[('Noted, for necessary action..!', 'Noted, for necessary action..!')], default='Unspecified', max_length=70),
        ),
        migrations.AlterField(
            model_name='checklist_trans_header',
            name='Quality_Engineer_status',
            field=models.CharField(choices=[('Well implimented Quality Checks', 'Well implimented Quality Checks'), ('Fairly implimented Quality Checks', 'Fairly implimented Quality Checks'), ('Poorly implimented Quality Checks', 'Poorly implimented Quality Checks')], default='Unspecified', max_length=70),
        ),
    ]
