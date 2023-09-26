from .models import Robot
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import send_robot_availability_email, send_robot_availability_email_to_console


@receiver(post_save, sender=Robot)  # Регистрация обработчика сигнала post_save для модели Robot
def notify_customer_on_robot_availability(sender, instance, created, **kwargs):
    if instance.available:  # Если установлен признак доступности робота
        robot_data = {
            'id': instance.id,
            'model': instance.model,
            'version': instance.version,
            'created': instance.created,

        }
        send_robot_availability_email.delay(robot_data)  # Асинхронная отправка уведомления о доступности робота
