# Generated by Django 4.1.7 on 2023-07-12 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0002_usermaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckList_Footer',
            fields=[
                ('CheckList_Item_ID', models.AutoField(primary_key=True, serialize=False)),
                ('CheckList_ID', models.IntegerField()),
                ('CheckList_Item_Desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CheckList_Header',
            fields=[
                ('CheckList_ID', models.AutoField(primary_key=True, serialize=False)),
                ('CheckList_Title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User_Rights',
            fields=[
                ('User_Rights_ID', models.AutoField(primary_key=True, serialize=False)),
                ('User_ID', models.IntegerField()),
                ('CheckList_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkapp.checklist_header')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CheckList_Trans_Header',
            fields=[
                ('Doc_ID', models.AutoField(primary_key=True, serialize=False)),
                ('inspection_Start_Date', models.DateTimeField(blank=True, null=True)),
                ('inspection_End_Date', models.DateTimeField(blank=True, null=True)),
                ('Contractor', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Structural_Element', models.CharField(max_length=100)),
                ('Quality_Engineer_status', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Well implimented Quality Checks'), ('2', 'Fairly implimented Quality Checks'), ('3', 'Poorly implimented Quality Checks')], default=None, max_length=70)),
                ('Project_Head_Status', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Yes'), ('2', 'No')], default=None, max_length=70)),
                ('CheckList_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkapp.checklist_header')),
                ('Project_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkapp.project_master')),
            ],
        ),
        migrations.CreateModel(
            name='CheckList_Trans_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doc_ID', models.IntegerField()),
                ('Site_Engineer_Status', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Yes'), ('2', 'No'), ('3', 'NA'), ('4', 'Partial')], default=None, max_length=70)),
                ('Site_DH_EQA_Status', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Yes'), ('2', 'No'), ('3', 'NA'), ('4', 'Partial')], default=None, max_length=70)),
                ('Site_Engineer_Comment', models.TextField()),
                ('Site_DH_EQA_Comment', models.TextField()),
                ('CheckList_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkapp.checklist_trans_header')),
                ('CheckList_Item_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkapp.checklist_footer')),
            ],
        ),
        migrations.AddField(
            model_name='checklist_footer',
            name='CheckList_Title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checklistID', to='checkapp.checklist_header'),
        ),
    ]
