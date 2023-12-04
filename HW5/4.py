# Есть ли статистически значимые различия в росте дочерей?
# Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169, 165
# Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160

import math
import scipy.stats as stats
import numpy as np

# списки роста
mat=np.array([172, 177, 158, 170, 178, 175, 164, 160, 169, 165])
doch=np.array([173, 175, 162, 174, 175, 168, 155, 170, 160, 163])
# длина списков
n1=len(mat)
n2=len(doch)
# средние значения
M1=np.mean(mat)
M2=np.mean(doch)
D1=np.var(mat, ddof=1)
D2=np.var(doch, ddof=1)
σ1=np.sqrt(D1)
σ2=np.sqrt(D2)

# 1. Формулирование гипотез:
# H0 - гипотеза, что статистически значимое различие в росте дочерей отсутствует
# H1 - гипотеза, что имеется статистически значимое различие в росте дочерей"

α=0.05
print(f"Выбор уровня статистической значимости:\n\
Выбираем параметр α={α}")

t1=stats.t.ppf(α/2,df=n1+n2-2)
t2=stats.t.ppf(1-α/2,df=n1+n2-2)
print(f'Выбор статистического критерия:\n\
Предполагая нормальное распределение и неизвестность σ \
генеральной совокупности, выбирается критерий Стьюдента.\n\
t1={t1}, t2={t2}')


t_diff=(M1-M2)/math.sqrt(D1/n1+D2/n2)
print(f'Расчет наблюдаемого критерия: t_diff=(M1-M2)/math.sqrt(D1/n1+D2/n2)={t_diff}')

print(f'Сравнение табличного и наблюдаемого значения:\n\
t1={t1}, t_diff={t_diff}, t2={t2}')

print(f'Вывод: Т.к. t1 < t_diff < t2, то гипотеза H0 верна. Статистически \
значимое различие в росте дочерей отсутствует.\n')

print(stats.ttest_rel(mat,doch))
print('p-value=0.52 > α=0.05, следовательно мы принимаем гипотезу H0')