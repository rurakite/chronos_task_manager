# Generated by Django 5.0 on 2023-12-29 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chronos', '0003_alter_worker_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
