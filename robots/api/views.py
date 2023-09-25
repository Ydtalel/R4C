from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from datetime import datetime

from ..models import Robot
from ..serializers import RobotSerializer


class CreateRobotView(APIView):
    def post(self, request):
        data = request.data
        try:
            model = data['model']
            version = data['version']
            created = datetime.strptime(data['created'], "%Y-%m-%d %H:%M:%S")

            # Валидация модели робота
            if not Robot.objects.filter(model=model).exists():
                raise ValidationError(f"Модель {model} не существует в системе.")

            # Далее будет добавлена логика валидации версии и других данных

            robot = Robot.objects.create(model=model, version=version, created=created)
            serializer = RobotSerializer(robot)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
