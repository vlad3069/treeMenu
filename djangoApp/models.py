from django.db import models


class MenuItem(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Заголовок')
    group = models.ForeignKey('self',
                              null=True,
                              blank=True,
                              related_name='menus',
                              on_delete=models.CASCADE,
                              verbose_name='Группа для меню')
    url = models.CharField(max_length=255,
                           null=False,
                           unique=True,
                           verbose_name='Адрес')
    named_url = models.CharField(max_length=255,
                                 null=True,
                                 blank=True)

    def __str__(self):
        return self.name[:15]
