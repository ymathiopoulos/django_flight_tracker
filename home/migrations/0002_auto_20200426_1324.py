# Generated by Django 2.1.5 on 2020-04-26 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InputNumbers',
        ),
        migrations.DeleteModel(
            name='OutputAnswer',
        ),
    ]