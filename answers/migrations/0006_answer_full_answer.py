# Generated by Django 4.1.4 on 2024-02-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0005_remove_answer_full_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='full_answer',
            field=models.TextField(blank=True, max_length=2500, null=True),
        ),
    ]
