# Generated by Django 4.1.7 on 2023-07-31 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0030_alter_checklist_trans_details_draft_site_dh_eqa_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist_trans_details_draft',
            name='Site_Engineer_Status',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Na', 'NA'), ('Partial', 'Partial')], default='Unspecified', max_length=70),
        ),
    ]
