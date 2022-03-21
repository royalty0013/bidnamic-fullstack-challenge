# Generated by Django 3.2 on 2022-03-11 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=500)),
                ('surname', models.CharField(max_length=500)),
                ('date_of_birth', models.DateField()),
                ('company_name', models.CharField(max_length=250)),
                ('address', models.TextField()),
                ('telephone', models.CharField(max_length=20)),
                ('bidding_settings', models.CharField(choices=[('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')], max_length=10)),
                ('google_ads_account_id', models.CharField(max_length=100)),
            ],
        ),
    ]
