# Generated by Django 3.0.5 on 2021-03-15 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0008_auto_20210315_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kit_numbers',
            name='id',
        ),
        migrations.AlterField(
            model_name='kit_numbers',
            name='welcome_kit_number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]