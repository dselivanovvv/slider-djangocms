# Generated by Django 3.2.13 on 2022-06-15 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_auto_20220615_2056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ('level',)},
        ),
    ]
