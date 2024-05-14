from django.db import models
from django.utils.text import gettext_lazy as _


class Delivery_Model(models.Model):
    name = models.ForeignKey('Supplier', on_delete=models.CASCADE, verbose_name=_("Название поставщика"),
                                          related_name='delivery_supplier', null=True, blank=True)
    who_pays = models.CharField('За чей счет', max_length=255, null=True, blank=True)
    postal_code = models.IntegerField('Почтовый индекс', null=True, blank=True)
    region = models.CharField("Регион", max_length=100, null=True, blank=True)
    city = models.CharField("Город", max_length=100, null=True, blank=True)
    address = models.CharField("Адрес", max_length=100, null=True, blank=True)
    middle_name = models.CharField("Фамилия", max_length=100, null=True, blank=True)
    first_name = models.CharField("Имя", max_length=100, null=True, blank=True)
    last_name = models.CharField("Отчество", max_length=100, null=True, blank=True)
    phone = models.CharField("Телефон", max_length=100, null=True, blank=True)
    email = models.CharField("Email", max_length=100, null=True, blank=True)
    
    def __str__(self):
        return str(self.name) + ' | ' + str(self.who_pays)
    
    class Meta:
        verbose_name = "Способ доставки"
        verbose_name_plural = "Способы доставки"
        

class Supplier(models.Model):
    name = models.CharField("Название поставщика", max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"