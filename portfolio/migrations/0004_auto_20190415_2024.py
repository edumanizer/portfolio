# Generated by Django 2.1.3 on 2019-04-15 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20190415_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='phonenumber',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
    ]
