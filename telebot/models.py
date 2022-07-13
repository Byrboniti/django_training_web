from django.db import models

# Create your models here.
class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='Чат')
    tg_massage = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.tg_chat # заменить название эелемента на имя из элемента
    class Meta:
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки' # меняем ордер на заказ и плюрал это множеметвенное число
