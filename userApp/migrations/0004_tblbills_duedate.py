# Generated by Django 3.1.5 on 2021-01-28 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0003_auto_20210128_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblbills',
            name='dueDate',
            field=models.CharField(default='1234:12:31', max_length=20),
        ),
    ]
