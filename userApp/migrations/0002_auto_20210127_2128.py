# Generated by Django 3.1.5 on 2021-01-27 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblmeters',
            name='installationDate',
            field=models.CharField(default='1234:12:31', max_length=15),
        ),
    ]
