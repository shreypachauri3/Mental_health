# Generated by Django 4.0.2 on 2022-03-05 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_basicinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='decision_maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]