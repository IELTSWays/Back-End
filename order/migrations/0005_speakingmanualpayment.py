# Generated by Django 4.1.4 on 2024-02-01 03:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_speakingtest_amount_speakingtest_authority_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0004_alter_manualpayment_transaction_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeakingManualPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_number', models.CharField(blank=True, max_length=255, null=True)),
                ('transaction_photo', models.ImageField(blank=True, null=True, upload_to='transaction')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('speaking', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.speakingtest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
