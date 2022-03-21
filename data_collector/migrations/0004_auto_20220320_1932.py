# Generated by Django 3.2 on 2022-03-20 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data_collector', '0003_rename_client_data_clientdata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientdata',
            options={'verbose_name_plural': 'Client Data'},
        ),
        migrations.AddField(
            model_name='clientdata',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]