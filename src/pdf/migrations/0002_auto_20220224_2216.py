# Generated by Django 3.2.12 on 2022-02-24 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='short_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='doc',
            name='step',
            field=models.CharField(choices=[('Not Started', 'Not Started'), ('Data Fetching', 'Data Fetching'), ('Mapping Fetching', 'Mapping Fetching'), ('Template Processing', 'Template Processing'), ('Doc Building', 'Doc Building'), ('Uploading', 'Uploading'), ('URL Shortening', 'URL Shortening'), ('Completed', 'Completed')], default='Not Started', max_length=30),
        ),
        migrations.AlterField(
            model_name='doc',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
