# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assigment', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=200)),
                ('dueDate', models.DateTimeField(verbose_name='Due date')),
                ('estHoursToComplete', models.DecimalField(decimal_places=2, max_digits=5)),
                ('actualHoursToComplete', models.DecimalField(decimal_places=2, max_digits=5)),
                ('complete', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='assignments',
            name='course',
            field=models.ForeignKey(to='tasks.Course'),
            preserve_default=True,
        ),
    ]
