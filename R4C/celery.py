from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установка переменной окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'R4C.settings')

# Создание экземпляра Celery
app = Celery('R4C')

# Загрузка настроек из конфигурации Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение и регистрация задач в приложениях Django
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Запущена задача Celery:', self.request.id)
