# Generated by Django 2.1.2 on 2018-10-06 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_city_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.District', verbose_name='bairro'),
        ),
    ]
