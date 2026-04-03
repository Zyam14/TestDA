# TestDA 
## Блок 1: Теория вероятности и логика
### Задание 1: Фермер
На ферме содержатся шесть разных видов животных, и каждый раз, когда фермер заходит в сарай, он видит одно случайное животное. За день фермер заходит в сарай 6 раз.
Каково математическое ожидание количества разных видов животных, которые фермер увидит за день?

### Ответ: 3,99

# Задание 2: Кулинарное соревнование
В конкурсе участвуют 80 шеф-поваров с уникальными уровнями мастерства. В первом этапе судьи случайным образом распределяют их по парам (в любом состязании двух шефов выигрывает тот, у кого выше уровень мастерства). На втором этапе шефы снова случайно образуют пары для финального раунда (пары могут повториться). Победную награду получают те, кто выиграл в обоих этапах.
Каково математическое ожидание числа победителей?

### Ответ: 26,84

### Задание 3: Одинокая дорога
На пустынном шоссе вероятность появления автомобиля за 30-минутный период составляет 0.95.
Какова вероятность его появления за 10 минут? А за 27 минут?

### Ответ: 0,63; 0,93

## Блок 2: Python
### Задание 1: Изоморфизмы
```
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

while True:
    s, t = str(input()), str(input())
    start = time.time()
    RESULT=is_isomorphic(s,t)
    end = time.time()
    print(RESULT)
    print("Время выполнения:", end - start)
```
### Вывод
```
привет
привет

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     25.8 MiB     25.8 MiB           1   @profile
     5                                         def is_isomorphic(s,t):
     6     25.8 MiB      0.0 MiB           1       s = s.lower()
     7     25.8 MiB      0.0 MiB           1       t = t.lower()
     8     25.8 MiB      0.0 MiB           1       dic = dict.fromkeys(s, "0")
     9                                         
    10     25.8 MiB      0.0 MiB           1       if len(s)!=len(t): return False
    11     25.8 MiB      0.0 MiB           7       for i in range(len(t)):
    12     25.8 MiB      0.0 MiB           6           if dic[s[i]]=="0": dic[s[i]]=t[i]
    13                                                 elif dic[s[i]]==t[i]: pass
    14                                                 else: return False
    15     25.8 MiB      0.0 MiB           1       return True


True
Время выполнения: 0.0141448974609375
```
Время выполнения 14 милисекунд - очень приемлемый результат. Память - 25 МБ - стандартные затраты для небольших программ на Python, особенно в которых есть создание словаря, что, скорее всего, и занимает всю память.

### Задание 2: Натуральная последовательность
```
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
```
### Вывод
```
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     5     25.6 MiB     25.6 MiB           1   @profile
     6                                         def find_abs(n):
     7     25.7 MiB      0.0 MiB           6       for i in (range(len(n)-1)):
     8     25.7 MiB      0.0 MiB           6           if n[i+1]-n[i]!=1: return n[i]+1
     9                                             return ("ок")
7
Время выполнения: 0.013200521469116211
```
Время выполнения и размер потраченной памяти аналогичны прошлому тесту, следовательно в этом тесте все значения также можно считать хорошими.

### Задание 3: Факторизация
```
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
```

### Вывод
```
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     5     25.7 MiB     25.7 MiB           1   @profile
     6                                         def find_factors(num):
     7     25.7 MiB      0.0 MiB           1        factors=[]
     8     25.7 MiB      0.0 MiB     1213407        for i in range(2,int(num**0.5)+1):
     9     25.7 MiB      0.0 MiB     1213410            while num%i==0:
    10     25.7 MiB      0.0 MiB           4                factors.append(i)
    11     25.7 MiB      0.0 MiB           4                num//=i
    12     25.7 MiB      0.0 MiB           1        if len(factors)==0: factors.append(num)
    13     25.7 MiB      0.0 MiB           1        return factors
[2, 1787, 5297, 77773]
Время выполнения: 23.248679161071777
```
Для такого огромного числа как 1 472 357 838 494, результат 23 секунды очень достойный. Использование памяти также очень мало так как она тратится только на массив результатов, который вовсе небольшой. 









