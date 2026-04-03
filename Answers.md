# TestDA 
## Блок 1: Теория вероятности и логика
### Задание 1: Фермер
Ответ: 3,99

### Задание 2: Кулинарное соревнование
Ответ: 26,84

### Задание 3: Одинокая дорога
Ответ: 0,63; 0,93

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
Файл _isomorph.py_

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
Файл _posled.py_

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
Файл _factors.py_ 

## Блок 3: SQL
### Задание 1: Абитуриенты
```
SELECT
    id, scores, RANK() OVER (ORDER BY scores DESC) AS position
FROM
    examination;
```

### Задание 2: FULL JOIN
Минимально 30 и максимально 50 строк.

### Задание 3: Покупки
```
SELECT a.client_id FROM account a JOIN transaction t ON a.id = t.account_id
WHERE t.transaction_date >= current_date - interval '1 month' AND t.type = 'buy'
GROUP BY a.client_id HAVING SUM(t.amount) < 5000;
```
## Блок 4: Статистика и АБ-тесты
### Задание 1: Воодушевленное руководство

* Тест нерепрезентативен, поэтому результаты применять по всей стране нельзя.
* Тест репрезентативен относительно своей генеральной совокупности: таких же небольших городов, можем применять только в подобных городах.
* Наличие эффекта подтвердило потенциал идеи, поэтому сразу применять по всем городам не будем, но можем провести эксперимент в других городах.

### Задание 2: Основной показатель в статистике

* Вероятность наблюдения такого или более экстремального результата при условии, что нулевая гипотеза верна.

### Задание 3: Параметрический тест

* Да, можем. При больших выборках t-тест устойчив к отклонению исходного распределения от нормального, поэтому его применение корректно.

## Блок 5: ML Base
### Задание 1: Пони тоже кони

Берём модель с ROC-AUC = 0.7, проверяем её на валидационной выборке, проводим улучшения: пробуем тонкую настройку гиперпараметров, добавляем или меняем признаки. 

### Задание 2: Ручной счёт ROC_AUC

#### Решение:
* расположим значения в порядке убывания и расставим ранги, в нашем случае от 14 до 1
* складываем ранги, где истинная метка равна 1 - (14 + 12 + 10 + 9 + 8 + 4 = 57)
* AUC=(сумма рангов положительных примеров - (P(P-1)/2))/P*N (36/48=0.75)
ROC-AUC = 0.75

### Задание 3: Ручной счёт корреляции

```
import numpy as np
from scipy.stats import pearsonr
x = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4]  # чашки кофе
y = [85, 88, 79, 81, 84, 65, 67, 58, 76, 49]  # баллы
r_matrix = np.corrcoef(x, y)  # возвращает матрицу корреляции
r = r_matrix[0, 1]  # коэффициент корреляции Пирсона
r, p_value = pearsonr(x, y)
print("r =", round(r, 2))
print("p-value =", round(p_value, 3))
```
Решение легче всего сделать с помощью библиотеки numpy. Выше код, который выводит значения:
``` 
r = -0.85
p-value = 0.002
```
Это значение p-value означает, что корреляция значима, а коэффициент Пирсона -0,85 показывает сильную обратную корреляцию (больше чашек кофе меньше балл). Нельзя утверждать причинно-следственную связь: корреляция показывает только связь, но не доказывает, что кофе напрямую снижает баллы.







