from __future__ import absolute_import, unicode_literals

# Подключение Celery к Django при загрузке приложения
from .celery import app as celery_app

__all__ = ('celery_app',)
