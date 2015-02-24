# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20150223_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='dueDate',
            field=models.DateField(verbose_name='Due date'),
            preserve_default=True,
        ),
    ]
