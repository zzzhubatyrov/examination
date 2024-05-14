from django.contrib import admin
from .models import Tasks, Facilities
from apps.user.models import Custom_User


admin.site.register(Facilities)


class Tasks_Admin(admin.ModelAdmin):
    list_display = ("service",  "name", "description", "date_creation", "date_end",
                    "status", 'applicants', 'appointeds', 'spectators')
    
    
    def applicants(self, obj):
        return "\n".join([str(user) for user in obj.applicant.all()])
    
    def appointeds(self, obj):
        return "\n".join([str(user) for user in obj.appointed.all()])
    
    def spectators(self, obj):
        return "\n".join([str(user) for user in obj.spectator.all()])
    
    
admin.site.register(Tasks, Tasks_Admin)