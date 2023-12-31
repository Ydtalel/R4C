import os
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from urllib.parse import quote

from .excel import generate_excel_report


def generate_report_view(request):
    try:
        generate_excel_report()
        file_path = 'robot_report.xlsx'

        if os.path.exists(file_path):
            with open(file_path, 'rb') as excel_file:
                response = HttpResponse(
                    excel_file.read(),
                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = f'attachment; filename="{quote("robot_report.xlsx")}"'
                return response
        else:
            return Response({'error': 'Файл отчета не найден'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
