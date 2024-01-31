# Generated by Django 4.1.4 on 2024-01-30 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover_photo',
        ),
        migrations.AddField(
            model_name='book',
            name='academic_cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='books'),
        ),
        migrations.AddField(
            model_name='book',
            name='general_cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='books'),
        ),
    ]
