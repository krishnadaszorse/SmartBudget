# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Full Name')),
                ('email', models.EmailField(max_length=50, verbose_name=b'Email')),
                ('password', models.CharField(max_length=50, verbose_name=b'Password')),
                ('phone', models.CharField(max_length=50, verbose_name=b'Phone')),
                ('avatar', models.ImageField(upload_to=b'', max_length=50, verbose_name=b'Avatar')),
                ('weekdays', models.CharField(max_length=100, null=True, verbose_name=b'Weekdays', choices=[(b'sun', b'Sunday'), (b'mon', b'Monday'), (b'tue', b'Tuesday'), (b'wed', b'Wednessday'), (b'Female', b'Female'), (b'Female', b'Female'), (b'Female', b'Female')])),
                ('country', models.CharField(max_length=100, null=True, verbose_name=b'Country', choices=[(b'IND', b'India')])),
                ('month_start_date', models.CharField(max_length=100, null=True, verbose_name=b'Month start Date', choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30')])),
                ('accounting_type', models.CharField(max_length=100, null=True, verbose_name=b'Accounting Type', choices=[(b'M2M', b'Month to Month'), (b'CON', b'Continuous')])),
                ('verification_key', models.CharField(max_length=50, verbose_name=b'Verification key')),
                ('key_generated', models.DateTimeField(max_length=50, verbose_name=b'Key generated')),
                ('is_verified', models.BooleanField(max_length=50, verbose_name=b'Verified')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'App User',
                'verbose_name_plural': 'App Users',
            },
            bases=(models.Model,),
        ),
    ]
