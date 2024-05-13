# Generated by Django 3.2.25 on 2024-05-12 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PromotionalPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('team', models.CharField(max_length=100)),
                ('medals', models.TextField()),
                ('product_to_promote', models.CharField(max_length=100)),
                ('promotion_paragraph', models.TextField()),
            ],
        ),
    ]
