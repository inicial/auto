from django.db import models


class Ad(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=128)
    desc = models.TextField(verbose_name='Описание', max_length=500, null=True)
    date = models.DateTimeField(verbose_name='Дата публикации', auto_now=True)
    cost = models.IntegerField(verbose_name='Цена', null=True)
    mileage = models.BigIntegerField(verbose_name='Пробег', null=True)
    year = models.CharField(verbose_name='Год', max_length=4)
    status = models.BooleanField(verbose_name='Статус объявления',)
    isHot = models.BooleanField(verbose_name='Срочное объявление',)
    images = models.ImageField(verbose_name='Изображение', upload_to='media/images/', null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/" % (self.id)

    class Meta:
        verbose_name = 'Обявление'
        verbose_name_plural = 'Обявления'

    def __str__(self):
        return self.title+' '+self.year+'#'+str(self.id)


class Comments(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=128)
    text = models.TextField(verbose_name='Комментарий', max_length=500, null=True)
    date = models.DateTimeField(verbose_name='Дата публикации', auto_now=True)
    status = models.BooleanField(verbose_name='Статус комментария', null=True,)
    adId = models.ManyToManyField(Ad, verbose_name='Объявление')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/%s/" % (self.id)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return str(self.id)
