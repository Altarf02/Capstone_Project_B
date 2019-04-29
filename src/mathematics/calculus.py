import numpy as np

def derivative(y, order):
    if order == 1:
        dy = np.diff(y)
        dx = 1
        derivative = dy/dx
    else:
        derivative = 0
    return derivative

def get_stationary_point_indexes(data):
    indexes = []
    temp_index = 0
    for val in data:
        if val == 0:
            indexes.append(temp_index)
        temp_index += 1
    return indexes

def count_zeros(data):
    count = 0
    for val in data:
        if val == 0:
            count += 1
    return count

def get_stationary_point_count(data, order):
    dy_dx = derivative(data, order)
    return count_zeros(dy_dx)
