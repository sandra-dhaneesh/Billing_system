# Generated by Django 4.2.3 on 2024-03-14 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BillSoftwareapp', '0002_remove_party_contact_remove_party_gst_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='party',
            name='gst_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
