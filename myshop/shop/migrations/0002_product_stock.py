# Generated by Django 4.1.10 on 2023-09-17 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]