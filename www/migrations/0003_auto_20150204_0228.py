# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='data',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
