import time
from memory_profiler import profile

@profile
def is_isomorphic(s,t):
    s = s.lower()
    t = t.lower()
    dic = dict.fromkeys(s, "0")

    if len(s)!=len(t): return False
    for i in range(len(t)):
        if dic[s[i]]=="0": dic[s[i]]=t[i]
        elif dic[s[i]]==t[i]: pass
        else: return False
    return True

s, t = str(input()), str(input())
start = time.time()
RESULT=is_isomorphic(s,t)
end = time.time()
print(RESULT)
print("Время выполнения:", end - start)





