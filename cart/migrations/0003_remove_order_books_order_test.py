# Generated by Django 4.1.4 on 2024-01-16 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
        ('cart', '0002_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='books',
        ),
        migrations.AddField(
            model_name='order',
            name='test',
            field=models.ManyToManyField(to='exam.test'),
        ),
    ]
