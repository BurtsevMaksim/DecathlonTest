from django.db import models
from decathlon.infrastracture import PointsCalculator


class Athlete(models.Model):
    name = models.CharField(max_length=200)
    result_100m = models.FloatField(max_length=200)
    result_long_jump = models.FloatField(max_length=200)
    result_shot_put = models.FloatField(max_length=200)
    result_high_jump = models.FloatField(max_length=200)
    result_400m = models.FloatField(max_length=200)
    result_110h = models.FloatField(max_length=200)
    result_discus = models.FloatField(max_length=200)
    result_pole_vault = models.FloatField(max_length=200)
    result_javelin = models.FloatField(max_length=200)
    result_1500m = models.FloatField(max_length=200)
    points_overall = models.IntegerField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.points_overall = PointsCalculator.calc_point_overall(self.result_100m, self.result_long_jump,
                                                                  self.result_shot_put, self.result_high_jump,
                                                                  self.result_400m, self.result_110h,
                                                                  self.result_discus,self.result_pole_vault,
                                                                  self.result_javelin, self.result_1500m)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name