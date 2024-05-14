from django.db import models
from apps.user.models import Custom_User
from django.utils.text import gettext_lazy as _



class Tasks(models.Model):
    service = models.CharField("Услуга", max_length=100)
    name = models.CharField("Заголовок", max_length=75)
    description = models.CharField("Описание", max_length=300, null=True, blank=True)
    facility = models.ForeignKey("Facilities", on_delete=models.CASCADE, related_name='facility_facilities', null=True, blank=True)
    address = models.ForeignKey("Facilities", on_delete=models.CASCADE, related_name='address_facilities', null=True, blank=True)
    applicant = models.ManyToManyField(Custom_User, related_name='applicant_user', blank=True)
    tags = models.CharField("Теги", max_length=50, null=True, blank=True) 
    deadline = models.DateTimeField("Дедлайн", blank=True, null=True)
    date_creation = models.DateTimeField("Плановый старт", auto_now_add=True, null=True)
    date_end = models.DateTimeField("Выполнить до", blank=True, null=True)
    appointed = models.ManyToManyField(Custom_User, related_name='appointed_user', blank=True)
    spectator = models.ManyToManyField(Custom_User, related_name='spectator_user', blank=True)
    labor_intensity = models.SmallIntegerField("Трудоемкость", blank=True)
    document = models.ManyToManyField("Documents_templates", related_name="documents_template_id", null=True, blank=True)
    status = models.ForeignKey("Tasks_Status", verbose_name=_("Статус"), on_delete=models.CASCADE, related_name='task_status', null=True, blank=True)
    
    
    def __str__(self):
        return self.service
    
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
    



class Facilities(models.Model):
    facility = models.CharField("Объект", max_length=100) 
    address = models.CharField("Адрес", max_length=50)

    def __str__(self):
        return self.facility + " | " + self.address
    
    class Meta:
        verbose_name = "Предприятие"
        verbose_name_plural = "Предприятия"
    

class Documents_templates(models.Model):
    document = models.FileField('Шаблон документа', upload_to='documents_templates', null=True)


    def __str__(self):
        return self.document.name
    
    def save(self, *args, **kwargs):
        super(Documents_templates, self).save(*args, **kwargs)
        
        # Retrieve the uploaded filename
        uploaded_filename = self.document.name
    
    
class Tasks_Status(models.Model):
    status = models.CharField("Статус", max_length=50)
    
    def __str__(self):
        return self.status
    
    
class Test(models.Model):
    test = models.FileField('Шаблон документа', upload_to='documents_templates')
    file_field_name = models.CharField('Название', max_length=75)

    def __str__(self):
        return self.test