# Generated by Django 3.1.3 on 2020-11-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0003_auto_20201126_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='deuration',
            field=models.DurationField(null=True),
        ),
    ]