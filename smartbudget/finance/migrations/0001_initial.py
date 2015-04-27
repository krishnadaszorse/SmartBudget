# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Transaction name')),
                ('transaction_date', models.DateTimeField(max_length=50, verbose_name=b'Transaction date')),
                ('amount', models.FloatField(verbose_name=b'Amount')),
                ('note', models.CharField(max_length=50, verbose_name=b'Note')),
                ('photo', models.ImageField(upload_to=b'', max_length=50, verbose_name=b'Photo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(verbose_name=b'Category ', to='master.Category', max_length=50)),
                ('user', models.ForeignKey(to='registration.AppUser')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
            bases=(models.Model,),
        ),
    ]
