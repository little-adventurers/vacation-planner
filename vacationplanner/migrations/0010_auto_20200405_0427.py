# Generated by Django 3.0 on 2020-04-05 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacationplanner', '0009_auto_20200405_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vacation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
