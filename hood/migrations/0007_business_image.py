# Generated by Django 3.2.5 on 2021-07-27 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0006_rename_business_name_business_business_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='image',
            field=models.ImageField(null=True, upload_to='business_pics'),
        ),
    ]
