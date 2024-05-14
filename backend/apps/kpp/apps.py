from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'apps.kpp'

    def ready(self):
        import apps.kpp.signals
        
        
        