# Generated by Django 3.0.4 on 2020-04-23 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_request'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Request',
        ),
        migrations.RemoveField(
            model_name='request_datetime',
            name='request_id',
        ),
        migrations.DeleteModel(
            name='Request_contact',
        ),
        migrations.DeleteModel(
            name='Request_Datetime',
        ),
    ]
