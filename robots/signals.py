from .models import Robot
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import send_robot_availability_email, send_robot_availability_email_to_console


@receiver(post_save, sender=Robot)
def notify_customer_on_robot_availability(sender, instance, created, **kwargs):
    if instance.available:
        # send_robot_availability_email(instance)
        send_robot_availability_email_to_console(instance)
