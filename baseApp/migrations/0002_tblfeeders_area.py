# Generated by Django 3.1.5 on 2021-01-26 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblfeeders',
            name='area',
            field=models.CharField(default=None, max_length=250),
        ),
    ]
