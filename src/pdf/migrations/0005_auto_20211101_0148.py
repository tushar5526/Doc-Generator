# Generated by Django 3.2.8 on 2021-10-31 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0004_auto_20211101_0139'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='audit',
            table='Audit',
        ),
        migrations.AlterModelTable(
            name='genericconfig',
            table='GenericConfig',
        ),
        migrations.AlterModelTable(
            name='pdf',
            table='Pdf',
        ),
    ]