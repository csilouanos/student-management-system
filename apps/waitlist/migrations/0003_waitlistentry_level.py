# Generated by Django 3.1.2 on 2020-11-02 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0002_auto_20201102_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='waitlistentry',
            name='level',
            field=models.IntegerField(default=1, verbose_name='Class Level'),
        ),
    ]