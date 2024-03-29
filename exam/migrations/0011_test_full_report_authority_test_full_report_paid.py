# Generated by Django 4.1.4 on 2024-03-25 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0010_test_confirm_test_confirm_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='full_report_authority',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='full_report_paid',
            field=models.BooleanField(default=False),
        ),
    ]
