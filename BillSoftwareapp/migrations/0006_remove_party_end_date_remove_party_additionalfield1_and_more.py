# Generated by Django 4.2.3 on 2024-03-15 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BillSoftwareapp', '0005_alter_history_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='End_date',
        ),
        migrations.RemoveField(
            model_name='party',
            name='additionalfield1',
        ),
        migrations.RemoveField(
            model_name='party',
            name='additionalfield2',
        ),
        migrations.RemoveField(
            model_name='party',
            name='additionalfield3',
        ),
        migrations.RemoveField(
            model_name='party',
            name='address',
        ),
        migrations.RemoveField(
            model_name='party',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='party',
            name='creditlimit',
        ),
        migrations.RemoveField(
            model_name='party',
            name='current_date',
        ),
        migrations.RemoveField(
            model_name='party',
            name='gst_no',
        ),
        migrations.RemoveField(
            model_name='party',
            name='last_updated_by',
        ),
        migrations.RemoveField(
            model_name='party',
            name='openingbalance',
        ),
        migrations.RemoveField(
            model_name='party',
            name='payment',
        ),
        migrations.AddField(
            model_name='party',
            name='opening_balance',
            field=models.FloatField(default=0),
        ),
    ]
