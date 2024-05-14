from django.db import models
from apps.taskpage.models import Tasks
from django.utils.text import gettext_lazy as _
from .models_consignee import Consignee_Model
from .models_delivery import Delivery_Model
from .models_equipment import Equipment_Model
from apps.user.models import Custom_User
from model_utils import FieldTracker



class KPP_Model(models.Model):
    name_number = models.CharField("Внешний номер", max_length=200, blank=True)
    name = models.CharField("Название организации", max_length=100, null=True, blank=True)
    description = models.CharField("Описаниие КПП", max_length=255, null=True, blank=True)
    tin = models.CharField("ИНН", max_length=50, null=True, blank=True)
    kpp = models.CharField("КПП", max_length=100, null=True, blank=True)
    сustomer_contact_person = models.CharField("Контактное лицо заказчика", max_length=200, null=True, blank=True)
    customer_phone = models.CharField("Телефон заказчика", max_length=200, null=True, blank=True)
    customer_email = models.CharField("Email заказчика", max_length=200, null=True, blank=True)
    consignee_details = models.ForeignKey(Consignee_Model, on_delete=models.CASCADE, verbose_name=_("Данные грузополучателя"),
                                          related_name='consignee_details', null=True, blank=True)
    delivery_method = models.ForeignKey(Delivery_Model, verbose_name=_("Способ доставки"),
                                        on_delete=models.CASCADE, related_name='delivery_method', null=True, blank=True)
    contract = models.CharField("Договор", max_length=200, null=True, blank=True)
    bill = models.CharField("Счет", max_length=200, null=True, blank=True)
    price = models.CharField("Стоимость", max_length=200, null=True, blank=True)
    payment_terms = models.CharField("Условия оплаты", max_length=200, null=True, blank=True)
    payment_order = models.CharField("Платежное поручение", max_length=200, null=True, blank=True)
    manager = models.ManyToManyField(Custom_User, related_name='manager_user', blank=True)
    sold_by = models.CharField("Продано от лица (организация)", max_length=200, null=True, blank=True)
    priority = models.SmallIntegerField( "Уровень приоритета", null=True, blank=True)
    difficulty = models.SmallIntegerField("Уровень сложности", null=True, blank=True)
    date_started = models.DateTimeField("Начало создание заявки", auto_now_add=True, null=True)
    date_end = models.DateTimeField("Дедлайн", null=True, blank=True)
    status = models.ForeignKey("KPP_STATUS", on_delete=models.CASCADE, related_name='kpp_status', null=True)
    status_tracker = FieldTracker(fields=['status'])
    document = models.ManyToManyField("KPP_Documents", related_name="docuemnts_kpp_id", blank=True)
    task = models.ManyToManyField(Tasks, verbose_name=_("Задачи"), related_name='kpp_tasks', blank=True)
    equipment = models.ManyToManyField(Equipment_Model, verbose_name=_("Оборудование"), related_name='kpp_equipment', blank=True)
    equipment_template = models.ManyToManyField("Equipment_Template", verbose_name=_("Шаблоны оборудования"), related_name='kpp_equipment_template', blank=True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "КПП"
        verbose_name_plural = "КПП"



class KPP_Status(models.Model):
    status = models.CharField("Статус", max_length=50, null=True, blank=True)


    def __str__(self):
        return self.status
    
    

class KPP_Documents(models.Model):
    document = models.FileField('Документ КПП', upload_to='documents_kpp')
    
    def __str__(self):
        return self.document.name
    
    def save(self, *args, **kwargs):
        super(KPP_Documents, self).save(*args, **kwargs)
        
        # Retrieve the uploaded filename
        uploaded_filename = self.document.name
        
        
        
class Equipment_Template(models.Model):
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
