# Generated by Django 2.1.1 on 2018-11-22 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad_avto', '0007_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='status',
            field=models.BooleanField(null=True, verbose_name='Статус комментария'),
        ),
    ]