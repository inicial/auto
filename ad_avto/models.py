from django.db import models


class Ad(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=128)
    date = models.DateTimeField(verbose_name='Дата публикации', auto_now=True)
    cost = models.IntegerField(verbose_name='Цена', null=True)
    mileage = models.BigIntegerField(verbose_name='Пробег', null=True)
    year = models.CharField(verbose_name='Год', max_length=4)
    status = models.BooleanField(verbose_name='Статус объявления',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/" % (self.id)

    class Meta:
        verbose_name = 'Обявление'
        verbose_name_plural = 'Обявления'

