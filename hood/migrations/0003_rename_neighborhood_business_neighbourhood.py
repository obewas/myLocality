# Generated by Django 3.2.5 on 2021-07-25 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0002_rename_location_neighbourhood_estate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='neighborhood',
            new_name='neighbourhood',
        ),
    ]
