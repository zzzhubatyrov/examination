from django.contrib import admin
from .models.models_kpp import KPP_Model, Delivery_Model
from .models.models_delivery import Supplier
from .models.models_consignee import Consignee_Model
from .models.models_equipment import Equipment_Model


class KPP_Admin(admin.ModelAdmin):
    list_display = ("name_number",  "name", "description", "priority", "difficulty",
                    "date_started", 'date_end', 'status','taskes')

    # def statuses(self, obj):
    #     return "\n".join([str(user) for user in obj.status.all()])
    
    def taskes(self, obj):
        return "\n | ".join([str(name) for name in obj.task.all()])

admin.site.register(Consignee_Model)
admin.site.register(Delivery_Model)
admin.site.register(Supplier)
admin.site.register(Equipment_Model)
admin.site.register(KPP_Model,  KPP_Admin)