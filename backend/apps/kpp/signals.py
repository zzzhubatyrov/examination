from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.models_kpp import KPP_Model

def action_for_status_one(instance):
    pass

def action_for_status_two(instance):
    pass

def action_for_status_three(instance):
    pass

def action_for_status_four(instance):
    pass

def action_for_status_five(instance):
    pass

status_action_mapping = {
    'Новый': action_for_status_one,
    'Обработка': action_for_status_two,
    'В процессе': action_for_status_three,
    'В работе': action_for_status_four,
    'ОТК': action_for_status_five,
}

@receiver(post_save, sender=KPP_Model)
def status_changed(sender, instance, **kwargs):
    if instance.status_tracker.has_changed('status'):
        action = status_action_mapping.get(instance.status)
        if action:
            action(instance)