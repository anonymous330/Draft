# Generated by Django 3.0.5 on 2021-03-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0005_demand_draft_dd_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_detain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custmer_name', models.CharField(max_length=20)),
                ('customer_dob', models.DateField(blank=True)),
                ('account_kit', models.IntegerField()),
                ('atm_kit', models.IntegerField()),
                ('adhaar_no', models.IntegerField()),
                ('mobile_no', models.IntegerField()),
                ('customer_father', models.CharField(max_length=20)),
                ('customer_mother', models.CharField(max_length=20)),
            ],
        ),
    ]
