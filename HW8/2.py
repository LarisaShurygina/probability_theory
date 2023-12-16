# Измерены значения IQ выборки студентов, обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

import scipy.stats as stats
import numpy as np

# список
iq = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
alpha=0.05
M=np.mean(iq)
D=np.var(iq)
n=len(iq)
t=stats.t.ppf(1-alpha/2,df=n-1)
U=M+t*np.sqrt(D/n)
L=M-t*np.sqrt(D/n)
print(f'Решение а:\n\
P({L} < {M} < {U})={1-alpha}')

# расчет доверительного интервала через stats
res=stats.t.interval(confidence=0.95, df=len(iq)-1, loc=np.mean(iq), scale=stats.sem(iq))
print(f'Решение б:\n\
{res}')
