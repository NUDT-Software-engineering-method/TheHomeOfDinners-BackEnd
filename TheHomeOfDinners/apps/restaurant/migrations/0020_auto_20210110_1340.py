# Generated by Django 3.1.3 on 2021-01-10 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0019_auto_20210110_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='菜品名称'),
        ),
    ]
