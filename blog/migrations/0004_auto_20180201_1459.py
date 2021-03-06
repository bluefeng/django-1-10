# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-01 14:59
from __future__ import unicode_literals

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180131_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='图片名(描述)')),
                ('head_pic', models.ImageField(upload_to='blog/', verbose_name='图片')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
            ],
            options={
                'verbose_name_plural': '图片',
                'ordering': ['-created'],
                'verbose_name': '图片',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '类别', 'verbose_name_plural': '类别'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '标签', 'verbose_name_plural': '标签'},
        ),
        migrations.AlterField(
            model_name='category',
            name='cover',
            field=models.ImageField(blank=True, upload_to='media/covers/categories/%Y/%m/%d/', verbose_name='封面(教程使用)'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cover_caption',
            field=models.CharField(blank=True, max_length=255, verbose_name='封面标题(教程使用)'),
        ),
        migrations.AlterField(
            model_name='category',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='category',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(1, '普通'), (2, '教程')], default=1, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='category',
            name='resource',
            field=models.URLField(blank=True, verbose_name='资源(废弃)'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='英文名'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, '进行中'), (2, '已完成')], null=True, verbose_name='状态(教程使用)'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, upload_to=blog.models.post_cover_path, verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.CharField(blank=True, max_length=255, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_time',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, '发布'), (2, '草稿'), (3, '隐藏'), (4, '秘密')], default=2, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='查看次数'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, verbose_name='名字'),
        ),
    ]
