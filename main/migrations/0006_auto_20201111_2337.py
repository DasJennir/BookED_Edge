# Generated by Django 3.1.3 on 2020-11-12 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_report_user_reported'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_user',
            name='reported',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
    ]
