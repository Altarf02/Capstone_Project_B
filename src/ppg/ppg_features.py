import statistics
from mathematics.calculus import *

def get_systolic_amplitude(data, no_of_samples, capture_duration):
    return max(data)

def get_p2p_interval(data, no_of_samples, capture_duration):
    normalized_data = []

    for i in range(no_of_samples):
        normalized_data.append(data[i] - 2048)
    
    dy_dx = derivative(data, order=1)
    
    # find points of maxima and minima
    stationary_points_i = get_stationary_point_indexes(dy_dx)
    stationary_points_vals = []

    max_vals = []
    min_vals = []

    # temp = 0
    # for i in range(0, no_of_samples):
    #     stationary_points_vals.append(normalized_data[stationary_points_i[temp]])
    #     temp += 1
    
    for i in stationary_points_vals:
        if i > 0:
            max_vals.append(i)
        elif i < 0:
            min_vals.append(i)

    return 3

def get_pulse_interval(data, no_of_samples, capture_duration):
    return 3

def get_bpm(data, no_of_samples, capture_duration):
    dy_dx = derivative(data, order=1)
    
    return 3

def get_ppg_features(data, no_of_samples, capture_duration):
    temp = []
    temp.append(int(statistics.mean(data)))
    temp.append(int(statistics.median(data)))
    temp.append(get_systolic_amplitude(data, no_of_samples, capture_duration))
    temp.append(get_p2p_interval(data, no_of_samples, capture_duration))
    temp.append(get_pulse_interval(data, no_of_samples, capture_duration))
    temp.append(get_bpm(data, no_of_samples, capture_duration))
    return temp