from decathlon.constansts import A_100M, B_100M, C_100M, A_LONG_JUMP, B_LONG_JUMP, C_LONG_JUMP, A_SHOT_PUT, B_SHOT_PUT, \
    C_SHOT_PUT, A_HIGH_JUMP, B_HIGH_JUMP, C_HIGH_JUMP, A_400M, B_400M, C_400M, A_110H, B_110H, C_110H, A_DISCUS, \
    B_DISCUS, C_DISCUS, A_POLE_VAULT, B_POLE_VAULT, C_POLE_VAULT, A_JAVELIN, B_JAVELIN, C_JAVELIN, A_1500M, B_1500M, \
    C_1500M
import csv


class PointsCalculator:

    @staticmethod
    def _calc_points_100m(result: float):
        return int(round((A_100M*((B_100M - result)**C_100M))))

    @staticmethod
    def _calc_points_long_jump(result: float):
        print((result - B_LONG_JUMP)**C_LONG_JUMP)
        print(type((result - B_LONG_JUMP)**C_LONG_JUMP))
        return int(round((A_LONG_JUMP*((result - B_LONG_JUMP)**C_LONG_JUMP))))

    @staticmethod
    def _calc_points_shot_put(result: float):
        return int(round((A_SHOT_PUT*((result - B_SHOT_PUT)**C_SHOT_PUT))))

    @staticmethod
    def _calc_points_high_jump(result: float):
        return int(round((A_HIGH_JUMP*((result - B_HIGH_JUMP)**C_HIGH_JUMP))))

    @staticmethod
    def _calc_points_400m(result: float):
        return int(round((A_400M*((B_400M - result)**C_400M))))

    @staticmethod
    def _calc_points_110h(result: float):
        return int(round((A_110H*((B_110H - result)**C_110H))))

    @staticmethod
    def _calc_points_discus(result: float):
        return int(round((A_DISCUS*((result - B_DISCUS)**C_DISCUS))))

    @staticmethod
    def _calc_points_pole_vault(result: float):
        return int(round((A_POLE_VAULT*((result - B_POLE_VAULT)**C_POLE_VAULT))))

    @staticmethod
    def _calc_points_javelin(result: float):
        return int(round((A_JAVELIN*((result - B_JAVELIN)**C_JAVELIN))))

    @staticmethod
    def _calc_points_1500m(result: float):
        return int(round((A_1500M*((B_1500M - result)**C_1500M))))

    @staticmethod
    def calc_point_overall(result_100m, result_long_jump, result_shot_put, result_high_jump, result_400m, result_110h,
                           result_discus, result_pole_vault, result_javelin, result_1500m):
        points_overall = PointsCalculator._calc_points_100m(result_100m) + \
                         PointsCalculator._calc_points_long_jump(result_long_jump) + \
                         PointsCalculator._calc_points_shot_put(result_shot_put) + \
                         PointsCalculator._calc_points_high_jump(result_high_jump) + \
                         PointsCalculator._calc_points_400m(result_400m) + \
                         PointsCalculator._calc_points_110h(result_110h) + \
                         PointsCalculator._calc_points_discus(result_discus) + \
                         PointsCalculator._calc_points_pole_vault(result_pole_vault) + \
                         PointsCalculator._calc_points_javelin(result_javelin) + \
                         PointsCalculator._calc_points_1500m(result_1500m)
        return points_overall


class FileProcessor:

    @staticmethod
    def get_data_from_csv(file):
        new_file =[]
        for row in csv.reader(file):
            row = row[0].split(sep=';')
            new_file.append(row)
        return [row for row in new_file]

