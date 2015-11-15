# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'songs')),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='song',
            fields=[
                ('picture', models.OneToOneField(primary_key=True, serialize=False, to='fileupload.Picture')),
                ('artist', models.CharField(default=b'artist', max_length=200, blank=True)),
                ('album', models.CharField(default=b'album', max_length=200, blank=True)),
                ('genre', models.CharField(default=b'genre', max_length=200, blank=True, choices=[(b'Alternative Music', b'Alternative Music'), (b'Blues', b' Blues'), (b'Classical Music', b'Classical Music'), (b'Country Music', b'Country Music')])),
                ('tag', models.CharField(default=b'tag', max_length=200, blank=True)),
            ],
        ),
    ]
