# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20150105_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentreply',
            name='owner',
            field=models.ForeignKey(to='news.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='commentreplyvote',
            name='voter',
            field=models.ForeignKey(to='news.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(to='news.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='owner',
            field=models.ForeignKey(to='news.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postcommentvote',
            name='voter',
            field=models.ForeignKey(to='news.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postvote',
            name='voter',
            field=models.ForeignKey(to='news.UserProfile'),
            preserve_default=True,
        ),
    ]
