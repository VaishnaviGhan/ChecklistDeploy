# Generated by Django 4.1.7 on 2023-09-12 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0044_checklist_trans_header_assigned_to_dheqa_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogDataNew',
            fields=[
                ('LogData_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Doc_ID', models.CharField(max_length=100)),
                ('Name_Of_ABLStaff', models.CharField(max_length=100)),
                ('assigned_to', models.CharField(max_length=100)),
                ('assigned_to_ProjectQA', models.CharField(max_length=100)),
                ('assigned_to_ProjectHead', models.CharField(max_length=100)),
                ('Date_Time', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='checklist_trans_header',
            name='checklist_status',
            field=models.CharField(choices=[('Completed_By_SiteEngineer & Pending_By_DHEQA', 'Completed_By_SiteEngineer & Pending_By_DHEQA'), ('Completed_By_SiteEngineer & Active_At_DHEQA', 'Completed_By_SiteEngineer & Active_At_DHEQA'), ('Completed_By_DHEQA & Pending_By_ProjectQA', 'Completed_By_DHEQA & Pending_By_ProjectQA'), ('Completed_By_DHEQA & Active_At_ProjectQA', 'Completed_By_DHEQA & Active_At_ProjectQA'), ('Completed_By_ProjectQA & Pending_By_ProjectHead', 'Completed_By_ProjectQA & Pending_By_ProjectHead'), ('Completed_By_ProjectQA & Active_At_ProjectHead', 'Completed_By_ProjectQA & Active_At_ProjectHead'), ('Completed_By_ProjectHead', 'Completed_By_ProjectHead')], max_length=70),
        ),
    ]
