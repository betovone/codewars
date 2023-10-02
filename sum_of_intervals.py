import pandas as pd

def sum_of_intervals(intervals):
    df = pd.DataFrame(intervals, columns=['start', 'end'])
    df = df.sort_values('start')
    suma = 0
    interval_tmp = min_start = max_end = None
    for interval in df.itertuples(1):
        if interval_tmp:
            if interval.start < min(min_start, interval_tmp.start):
                suma += interval_tmp.start - interval.start
                min_start = interval_tmp.start
                
            if interval.start > max_end < interval.end:
                max_end = interval.start
            
            if max(interval_tmp.end, max_end) < interval.end:
                suma += interval.end - max(max_end, interval_tmp.end)
                max_end = interval.end
            
        else:
            min_start = interval.start
            max_end = interval.end
            suma += interval.end - interval.start
            
        # print(suma)
        interval_tmp = interval
    return suma

if __name__ == "__main__":
    assert sum_of_intervals([(1, 5)]) == 4
    assert sum_of_intervals([(1, 5), (6, 10)])== 8
    assert sum_of_intervals([(1, 5), (1, 5)])== 4
    assert sum_of_intervals([(1, 4), (7, 10), (3, 5)])== 7
    assert sum_of_intervals([(-1000000000, 1000000000)])== 2000000000
    assert sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)])== 100_000_030
    assert sum_of_intervals([(10, 462), (45, 402), (107, 456), (270, 453), (234, 268), (224, 264)]) == 452
