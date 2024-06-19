import math


def calculate_info(prob: float) -> float:
    return -prob * math.log2(prob)
