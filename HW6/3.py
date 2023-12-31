# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.

import scipy.stats as stats
import numpy as np

α=0.05
doch=np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
mat=np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
D1=np.var(doch,ddof=1)
D2=np.var(mat,ddof=1)
σ1=np.sqrt(D1)
σ2=np.sqrt(D2)
M1=np.mean(doch)
M2=np.mean(mat)
n1=len(doch)
n2=len(mat)


# находим дельту
delta=M1-M2
# объединенная оценка дисперсии
D=(D1+D2)/2
Sdelta=np.sqrt(D/n1+D/n2)
t=stats.t.ppf(1-α/2,df=n1+n2-2)

L=delta-t*Sdelta
U=delta+t*Sdelta

print(f'P({L} < delta < {U})={1-α}')