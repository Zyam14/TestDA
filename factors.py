import time
from memory_profiler import profile

n=1472357838494
@profile
def find_factors(num):
     factors=[]
     for i in range(2,int(num**0.5)+1):
         while num%i==0:
             factors.append(i)
             num//=i
     if len(factors)==0: factors.append(num)
     return factors


start = time.time()
result=find_factors(n)
end = time.time()
print(result)
print("Время выполнения:", end - start)