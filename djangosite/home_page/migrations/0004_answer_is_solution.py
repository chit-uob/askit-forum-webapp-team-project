# Generated by Django 4.1.7 on 2023-03-08 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0003_answer_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_solution',
            field=models.BooleanField(default=False),
        ),
    ]
