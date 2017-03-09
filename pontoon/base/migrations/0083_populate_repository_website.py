# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 12:43
from __future__ import unicode_literals

import re

from django.db import migrations


def populate_repository_website(apps, schema_editor):
    Repository = apps.get_model('base', 'Repository')
    for repository in Repository.objects.all():
        repository.website = (
            re.sub(re.escape('.git') + '$', '', repository.url)
            .replace('git@github.com:', 'https://github.com/')
            .replace('ssh://', 'https://')
        )
        repository.save()


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0082_auto_20170217_1231'),
    ]

    operations = [
        migrations.RunPython(populate_repository_website, migrations.RunPython.noop),
    ]
