# Generated by Django 3.2.13 on 2022-06-15 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='contact_period',
            new_name='contract_period',
        ),
    ]
