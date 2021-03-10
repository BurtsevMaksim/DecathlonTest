from rest_framework import serializers
from decathlon.models import Athlete


class AthleteSerializer(serializers.ModelSerializer):

    place = serializers.SerializerMethodField()

    class Meta:
        model = Athlete
        fields = ('id', 'name', 'result_100m', 'result_long_jump', 'result_shot_put', 'result_high_jump',
                  'result_400m', 'result_110h', 'result_discus', 'result_pole_vault', 'result_javelin',
                  'result_1500m', 'points_overall', 'place')
    # This is an absolutely horrific piece of a code, that i would never use in production.
    # The only reason it exists - is to accomplish task(about naming places of athletes), described in test.
    def get_place(self, obj):
        d = Athlete.objects.all().order_by('-points_overall')
        list_d = list(d.values_list('points_overall', flat=True))
        ath_points_index = list_d.index(obj.points_overall)
        dict_of_elems = dict()
        index = 0
        for item in list_d:
            if item == obj.points_overall:
                if item in dict_of_elems:
                    dict_of_elems[item][0] += 1
                    dict_of_elems[item][1].append(index+1)
                else:
                    dict_of_elems[item] = [1, [index+1]]
                index += 1
        dict_of_elems = {key: value for key, value in dict_of_elems.items() if value[0] > 1}
        if len(dict_of_elems.items()) > 0:
            print(dict_of_elems.items())
            return f"{dict_of_elems.get(obj.points_overall)[1][0]}-{dict_of_elems.get(obj.points_overall)[1][1]}"
        return ath_points_index+1