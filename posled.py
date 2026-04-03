import time
from memory_profiler import profile

nums = [1, 2, 3,4, 5, 6,8]
@profile
def find_abs(n):
    for i in (range(len(n)-1)):
        if n[i+1]-n[i]!=1: return n[i]+1
    return ("ок")

start = time.time()
result=find_abs(nums)
end = time.time()
print(result)
print("Время выполнения:", end - start)

