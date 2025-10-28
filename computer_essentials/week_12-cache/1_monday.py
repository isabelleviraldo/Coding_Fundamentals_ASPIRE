import time
import random

N = 2000000
data1 = [i for i in range(N)]
data2 = [i for i in range(N)]
data3 = [data1, data2]



start1 = time.perf_counter()
total1 = 0
for i in range(1):
    for j in range(N):
        total1 += data3[i][j]

end1 = time.perf_counter()
print(f"adding 1: {end1 - start1}")



start2 = time.perf_counter()
total2 = 0
for j in range(N):
    for i in range(1):
        total2 += data3[i][j]

end2 = time.perf_counter()
print(f"adding 2: {end2 - start2}")