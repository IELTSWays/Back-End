# Generated by Django 4.1.4 on 2024-01-03 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_user_national_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='province',
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
