# Generated by Django 2.2 on 2022-01-26 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20220126_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
