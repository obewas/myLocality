# Generated by Django 3.2.5 on 2021-07-23 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField()),
                ('posted_by', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]