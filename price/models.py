from django.db import models

# Create your models here.
class PriceCard(models.Model):
    pc_value = models.CharField(max_length=20, verbose_name= 'Цена')
    pc_description = models.CharField(max_length=200, verbose_name= 'Описание')

    def __str__(self):
        return self.pc_value  # заменить название эелемента на имя из элемента

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'  # меняем ордер на заказ и плюрал это множеметвенное число


class PriceTable(models.Model):
    pt_title = models.CharField(max_length=20, verbose_name= 'услуга')
    pt_old_price = models.CharField(max_length=20, verbose_name= 'Старая Цена')
    pt_new_price = models.CharField(max_length=20, verbose_name= 'Новая цена')

    def __str__(self):
        return self.pt_title  # заменить название эелемента на имя из элемента

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'  # меняем ордер на заказ и плюрал это множеметвенное число