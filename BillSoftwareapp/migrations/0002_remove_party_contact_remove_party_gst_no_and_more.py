# Generated by Django 4.2.3 on 2024-03-14 09:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BillSoftwareapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='party',
            name='gst_no',
        ),
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 14)),
        ),
    ]
