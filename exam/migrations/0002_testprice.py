# Generated by Django 4.1.4 on 2024-01-22 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listening', models.IntegerField(default=0)),
                ('reading', models.IntegerField(default=0)),
                ('writing', models.IntegerField(default=0)),
                ('speaking', models.IntegerField(default=0)),
            ],
        ),
    ]
