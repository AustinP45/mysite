# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20150210_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('task', models.CharField(max_length=80)),
                ('desc', models.CharField(max_length=200)),
                ('dueDate', models.DateTimeField(verbose_name='Due date')),
                ('estHrsToComplete', models.DecimalField(max_digits=5, decimal_places=2)),
                ('actHrsToComplete', models.DecimalField(max_digits=5, decimal_places=2)),
                ('complete', models.BooleanField(default=False)),
                ('course', models.ForeignKey(to='tasks.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='assignments',
            name='course',
        ),
        migrations.DeleteModel(
            name='Assignments',
        ),
    ]
