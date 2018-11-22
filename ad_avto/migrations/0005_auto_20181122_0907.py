# Generated by Django 2.1.1 on 2018-11-22 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad_avto', '0004_ad_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'verbose_name': 'Обявление', 'verbose_name_plural': 'Обявления'},
        ),
        migrations.AddField(
            model_name='ad',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='cost',
            field=models.IntegerField(null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='mileage',
            field=models.BigIntegerField(null=True, verbose_name='Пробег'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='status',
            field=models.BooleanField(verbose_name='Статус объявления'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='year',
            field=models.CharField(max_length=4, verbose_name='Год'),
        ),
    ]
