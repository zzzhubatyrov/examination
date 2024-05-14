from django.db import models
from django.utils.text import gettext_lazy as _



class Equipment_Model(models.Model):
    name = models.CharField("Наименование оборудования", max_length=250, null=True, blank=True)
    specifications = models.TextField("Технические характеристики", null=True, blank=True)
    delivery_set = models.TextField("Комплект доставки", null=True, blank=True)
    documentation_set = models.TextField("Комплект документации", null=True, blank=True)
    documentation_set_before_bs = models.TextField("Комплект документации до отгрузки", null=True, blank=True)
    examination = models.CharField("Проверка", max_length=250, null=True, blank=True)
    samples = models.CharField("Образцы", max_length=250, null=True, blank=True)
    consignment_note = models.CharField("Товарная накладная", max_length=250, null=True, blank=True)
    pnr = models.BooleanField("ПНР", null=True, blank=True)
    installation_supervision = models.CharField("Служба установки", max_length=250, null=True, blank=True) 
    guarantee = models.CharField("Гарантия", max_length=250, null=True, blank=True)
    year_of_manufacture = models.CharField("Год выпуска", max_length=100, null=True, blank=True)
    factory_number = models.CharField("Заводской номер", max_length=100, null=True, blank=True)
    shipment_time = models.DateTimeField("Срок отгрузки", null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"
         
