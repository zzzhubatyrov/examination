from django.db import models



class Consignee_Model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название организации", max_length=100, null=True, blank=True)
    tin = models.CharField("ИНН", max_length=50, null=True, blank=True)
    kpp = models.CharField("КПП", max_length=100, null=True, blank=True)
    postal_code = models.IntegerField("Почтовый индекс", null=True, blank=True)
    region = models.CharField("Регион", max_length=100, null=True, blank=True)
    city = models.CharField("Город", max_length=100, null=True, blank=True)
    address = models.CharField("Адрес", max_length=100, null=True, blank=True)
    middle_name = models.CharField("Фамилия", max_length=100, null=True, blank=True)
    first_name = models.CharField("Имя", max_length=100, null=True, blank=True)
    last_name = models.CharField("Отчество", max_length=100, null=True, blank=True)
    phone = models.CharField("Телефон", max_length=100, null=True, blank=True)
    email = models.CharField("Email", max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Грузополучатель"
        verbose_name_plural = "Грузополучатель"