# Generated by Django 3.0.5 on 2020-09-26 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0003_farmer_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='number_register',
            name='place',
            field=models.CharField(default='yes', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='number_register',
            name='status',
            field=models.CharField(default='place', max_length=50),
            preserve_default=False,
        ),
    ]
