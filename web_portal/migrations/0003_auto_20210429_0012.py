# Generated by Django 3.1.8 on 2021-04-28 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('web_portal', '0002_speciality_specialitylist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_page_link', to='cms.page'),
        ),
    ]