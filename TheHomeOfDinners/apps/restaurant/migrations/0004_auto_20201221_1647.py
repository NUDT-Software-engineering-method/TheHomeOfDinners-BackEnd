# Generated by Django 3.1.2 on 2020-12-21 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0003_auto_20201206_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant_collection', to='restaurant.restaurant', verbose_name='所属餐馆'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_collection', to=settings.AUTH_USER_MODEL, verbose_name='评论发布者'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='restaurant.restaurant', verbose_name='所属餐馆'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='owner',
            field=models.CharField(choices=[('1', '餐馆图片'), ('2', '菜单图片'), ('3', '评论图片')], max_length=1, verbose_name='图片创建者'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant', to=settings.AUTH_USER_MODEL, verbose_name='餐馆创建者'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='verify',
            field=models.CharField(choices=[('0', '审核中'), ('1', '审核通过'), ('-1', '审核未通过')], default='0', max_length=2, verbose_name='审核状态(0-审核中，1-审核通过，-1-审核未通过)'),
        ),
        migrations.AlterField(
            model_name='review',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_review', to='restaurant.restaurant', verbose_name='所属餐馆'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_review', to=settings.AUTH_USER_MODEL, verbose_name='评论发布者'),
        ),
    ]
