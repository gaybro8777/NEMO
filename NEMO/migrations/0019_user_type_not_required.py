# Generated by Django 2.2.10 on 2020-05-29 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0018_area_count_staff_in_occupancy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NEMO.UserType'),
        ),
    ]