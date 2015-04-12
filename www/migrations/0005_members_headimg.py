# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0004_auto_20150326_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='headimg',
            field=models.FileField(default=datetime.datetime(2015, 3, 30, 6, 45, 50, 959241, tzinfo=utc), upload_to=b'./upload/'),
            preserve_default=False,
        ),
    ]
