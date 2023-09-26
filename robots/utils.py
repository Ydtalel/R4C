from django.core.mail import send_mail
from R4C.settings import EMAIL_HOST_USER
from orders.models import Order
from celery import shared_task

from django.conf import settings

from robots.models import Robot


# def send_robot_availability_email(robot):
#     orders = Order.objects.filter(robot_serial=robot.serial)
#     if orders:
#         for order in orders:
#             subject = "Робот доступен в наличии"
#             message = f"Добрый день!\n\nНедавно вы интересовались нашим роботом модели {robot.model}, " \
#                       f"версии {robot.version}.\n\nЭтот робот теперь в наличии. Если вам подходит этот " \
#                       f"вариант - пожалуйста, свяжитесь с нами."
#             send_mail(subject, message, EMAIL_HOST_USER, [order.customer.email])


# Отправить письмо с использованием настроек из settings.py
def send_robot_availability_email_to_console(robot):
    orders = Order.objects.filter(robot_serial=robot.serial)
    if orders:
        for order in orders:
            subject = "Робот доступен в наличии"
            message = f"Добрый день!\n\nНедавно вы интересовались нашим роботом модели {robot.model}, " \
                      f"версии {robot.version}.\n\nЭтот робот теперь в наличии. Если вам подходит этот " \
                      f"вариант - пожалуйста, свяжитесь с нами."

            send_mail(subject, message, 'example@mail.com', ['reciever@mail.com'])


@shared_task
def send_robot_availability_email(robot_data):
    robot = Robot.objects.get(id=robot_data['id'])  # Получаем объект робота по его ID
    orders = Order.objects.filter(robot_serial=robot.serial)
    if orders:
        for order in orders:
            subject = "Робот доступен в наличии"
            message = f"Добрый день!\n\nНедавно вы интересовались нашим роботом модели {robot.model}, " \
                      f"версии {robot.version}.\n\nЭтот робот теперь в наличии. Если вам подходит этот " \
                      f"вариант - пожалуйста, свяжитесь с нами."
            send_mail(subject, message, EMAIL_HOST_USER, [order.customer.email])
