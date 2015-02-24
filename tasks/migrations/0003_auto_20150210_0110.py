# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20150210_0045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignments',
            old_name='assigment',
            new_name='assignment',
        ),
    ]
