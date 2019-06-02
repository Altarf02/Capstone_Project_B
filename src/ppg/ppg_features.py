import statistics
from mathematics.calculus import *
import math

def get_systolic_amplitude(data, no_of_samples, capture_duration):
    return max(data)

def get_p2p_interval(data, no_of_samples, capture_duration):

    data = data[0:100]

    max_1 = data[0]
    max_1_index = 0
    max_2 = 0
    max_2_index = 0

    for i in range(1, 100):
        if (data[i] > max_1):
            max_2 = max_1
            max2_index = max_1_index
            max_1 = data[i]
            max_1_index = i

    diff = abs(max_2_index - max_1_index)

    p2p_interval_in_sec = diff * (capture_duration / no_of_samples)

    return p2p_interval_in_sec

def get_pulse_interval(data, no_of_samples, capture_duration):

    data = data[0:100]

    min_1 = data[0]
    min_1_index = 0
    min_2 = 0
    min_2_index = 0

    for i in range(1, 100):
        if (data[i] < min_1):
            min_2 = min_1
            min2_index = min_1_index
            min_1 = data[i]
            min_1_index = i

    diff = abs(min_2_index - min_1_index)

    pulse_interval = diff * (capture_duration / no_of_samples)

    return pulse_interval

def get_bpm(data, no_of_samples, capture_duration):
    
    temp = get_p2p_interval(data, no_of_samples, capture_duration)

    return 60 / temp

def get_ppg_features(data, no_of_samples, capture_duration):
    temp = []
    temp.append(int(statistics.mean(data)))
    temp.append(int(statistics.median(data)))
    temp.append(int( 4096 * math.sin(statistics.mean(data))))
    temp.append(int( 4096 * math.cos(statistics.mean(data))))
    temp.append(int( 4096 * math.sin(statistics.mean(data)) * math.sin(statistics.mean(data)) ))
    temp.append(int( 4096 * math.cos(statistics.mean(data)) * math.cos(statistics.mean(data)) ))
    # temp.append(get_systolic_amplitude(data, no_of_samples, capture_duration))
    # temp.append(get_p2p_interval(data, no_of_samples, capture_duration))
    # temp.append(get_pulse_interval(data, no_of_samples, capture_duration))
    # temp.append(get_bpm(data, no_of_samples, capture_duration))
    return temp