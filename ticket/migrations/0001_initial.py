# Generated by Django 4.1.4 on 2023-12-04 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('status', models.CharField(choices=[('new', 'new'), ('pending', 'pending'), ('canceled', 'canceled'), ('completed', 'completed')], default='New', max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]