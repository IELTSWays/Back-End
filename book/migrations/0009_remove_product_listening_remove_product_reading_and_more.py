# Generated by Django 4.1.4 on 2024-01-31 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_remove_product_skill_product_listening_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='listening',
        ),
        migrations.RemoveField(
            model_name='product',
            name='reading',
        ),
        migrations.RemoveField(
            model_name='product',
            name='writing',
        ),
    ]
