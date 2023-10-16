# Generated by Django 4.1.7 on 2023-07-12 04:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_ID', models.IntegerField()),
                ('Department_ID', models.IntegerField()),
                ('Project_ID', models.IntegerField()),
                ('Site_ID', models.IntegerField()),
                ('Department_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkapp.department')),
                ('Project_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkapp.project_master')),
                ('Site_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkapp.site_master')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]