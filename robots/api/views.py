from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from datetime import datetime

from ..models import Robot
from ..serializers import RobotSerializer

from django.core.cache import cache


class CreateRobotView(APIView):
    def post(self, request):
        data = request.data
        try:
            model = data['model']
            version = data['version']
            created = datetime.strptime(data['created'], "%Y-%m-%d %H:%M:%S")

            # Пробуем получить информацию о модели из кэша
            robot = cache.get(model)

            if robot is None:
                # Если данных в кэше нет, выполняем запрос к базе данных
                robot = Robot.objects.create(model=model, version=version, created=created)
                print("Данные взяты из базы данных")

                # Сохраняем информацию в кэше
                cache.set(model, robot, 300)  # Здесь 300 - время кэширования в секундах
            else:
                print("Данные взяты из кэша")

            serializer = RobotSerializer(robot)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
