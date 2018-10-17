import filter
import numpy as np

def metrics(data_list):
    sizes = []
    times = []
    for data in data_list:
        sizes.append(np.array(data.totalByte))
        times.append(np.array(data.TotalTime))
    npSizes = np.array(sizes)
    npTimes = np.array(times)

    size_std_dev = np.std(npSizes)
    size_avg = np.average(npSizes)
    time_std_dev = np.std(npTimes)
    time_avg = np.average(npTimes)