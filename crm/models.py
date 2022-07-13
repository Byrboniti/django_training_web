from django.db import models

# Create your models here.
class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='название статуса')

    def __str__(self):
        return self.Status_name # заменить название эелемента на имя из элемента
    class Meta:
        verbose_name = 'Сататус'
        verbose_name_plural = 'Статусы' # меняем ордер на заказ и плюрал это множеметвенное число


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name= 'Имя')
    order_phone = models.CharField(max_length=200, verbose_name= 'Телефон')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')
    def __str__(self):
        return self.order_name # заменить название эелемента на имя из элемента
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы' # меняем ордер на заказ и плюрал это множеметвенное число


class ComentCrm(models.Model):
    coment_binding = models.ForeignKey(Order, on_delete=models.CASCADE,  verbose_name='Заявка')
    coment_text = models.TextField(verbose_name='Текст комментария')
    coment_dt = models.DateTimeField(auto_now = True, verbose_name= 'Дата каментария')

    def __str__(self):
        return self.coment_text # заменить название эелемента на имя из элемента
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии' # меняем ордер на заказ и плюрал это множеметвенное число