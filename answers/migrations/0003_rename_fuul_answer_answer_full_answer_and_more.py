# Generated by Django 4.1.4 on 2024-02-21 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0002_testfullcorrectanswer_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='fuul_answer',
            new_name='full_answer',
        ),
        migrations.AddField(
            model_name='answer',
            name='question_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]