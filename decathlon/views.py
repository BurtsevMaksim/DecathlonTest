from django.shortcuts import render
from decathlon.infrastracture import FileProcessor
from io import TextIOWrapper
from decathlon.serializers import AthleteSerializer
from rest_framework import viewsets
from decathlon.models import Athlete


class AthleteViewSet(viewsets.ModelViewSet):
    serializer_class = AthleteSerializer
    queryset = Athlete.objects.all().order_by('-points_overall')


def athlete_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        file = TextIOWrapper(request.FILES['myfile'].file, encoding=request.encoding)
        for row in FileProcessor.get_data_from_csv(file):
            seconds = row[10].split('.', 1)
            seconds = (int(seconds[0]) * 60) + float(seconds[1])
            _, created = Athlete.objects.get_or_create(
                name=row[0],
                result_100m=float(row[1]),
                result_long_jump=float(row[2])*100,
                result_shot_put=float(row[3]),
                result_high_jump=float(row[4])*100,
                result_400m=float(row[5]),
                result_110h=float(row[6]),
                result_discus=float(row[7]),
                result_pole_vault=float(row[8])*100,
                result_javelin=float(row[9]),
                result_1500m=seconds
            )
        return render(request, 'athlete_upload.html')
    return render(request, 'athlete_upload.html')
