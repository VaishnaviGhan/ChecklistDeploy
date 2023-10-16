# Generated by Django 4.1.7 on 2023-07-13 12:31

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0007_alter_checklist_footer_checklist_item_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist_trans_header',
            name='Project_Head_Status',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Yes'), ('2', 'No')], default=None, max_length=70),
        ),
        migrations.AlterField(
            model_name='checklist_trans_header',
            name='Quality_Engineer_status',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Well implimented Quality Checks'), ('2', 'Fairly implimented Quality Checks'), ('3', 'Poorly implimented Quality Checks')], default=None, max_length=70),
        ),
    ]
