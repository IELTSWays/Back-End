# Generated by Django 4.1.4 on 2024-04-25 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_remove_user_wrong_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
