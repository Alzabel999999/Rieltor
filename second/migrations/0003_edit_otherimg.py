# Generated by Django 2.1.11 on 2020-03-16 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0002_auto_20200316_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='edit',
            name='otherimg',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
