# Generated by Django 4.1.4 on 2023-12-21 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(default='teachers/default.png', upload_to='teachers'),
        ),
    ]
