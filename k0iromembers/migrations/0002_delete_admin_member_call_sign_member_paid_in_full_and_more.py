# Generated by Django 5.1.7 on 2025-03-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('k0iromembers', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.AddField(
            model_name='member',
            name='call_sign',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='paid_in_full',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
