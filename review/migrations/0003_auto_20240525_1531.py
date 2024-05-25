# Generated by Django 3.2.25 on 2024-05-25 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_drop_review_recommend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='review',
            name='recommend',
        ),
    ]
