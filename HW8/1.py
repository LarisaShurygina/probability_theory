# Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy.
# Полученные значения должны быть равны. Найдите коэффициент корреляции Пирсона с помощью ковариации
# и среднеквадратичных отклонений двух признаков, а затем с использованием функций из библиотек numpy и pandas.

import scipy.stats as stats
import numpy as np

# списки
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]
npzp = np.array(zp)
npks = np.array(ks)

# длина списка
n=len(zp)

# расчет среднего арифметического зарплаты
Mzp=0
for i in zp:
    Mzp+=i
Mzp/=n

# расчет несмещенной дисперсии зарплаты
summa_delta=0
for i in zp:
    summa_delta+=(i-Mzp)**2
# несмещенная дисперсия
Dzp=summa_delta/(n-1)
# среднеквадратичное отклонение зарплаты
σzp=np.sqrt(Dzp)

# расчет среднего арифметического кредитного скоринга
Mks=0
for i in ks:
    Mks+=i
Mks/=n

# расчет несмещенной дисперсии кредитного скоринга
summa_delta=0
for i in ks:
    summa_delta+=(i-Mks)**2
# несмещенная дисперсия
Dks=summa_delta/(n-1)
# среднеквадратичное отклонение кредитного скоринга
σks=np.sqrt(Dks)

# расчет среднего арифметического произведения zp и ks
Mzpks=0
for i in range(n):
    Mzpks+=zp[i]*ks[i]
Mzpks/=n

#print(Mzp,np.mean(npzp), Mks,np.mean(npks), Mzpks,np.mean(npzp*npks))
COVzpks=Mzpks-Mzp*Mks
print(f"Решение задачи 1.\n\
1. Расчет ковариации вручную COVxy=M(x*y)-M(x)*M(y): {COVzpks}\n\
Еще вариант расчета вручную: {np.mean(npzp*npks)-np.mean(npzp)*np.mean(npks)}\n\
2a. Расчет смещенной ковариации через функцию np.cov: {np.cov(npzp,npks,ddof=0)[0][1]}\n\
2б. Расчет несмещенной ковариации через функцию np.cov: {np.cov(npzp,npks,ddof=1)[0][1]}")

print(f'3. Расчет коэффициента Пирсона вручную: {np.cov(npzp,npks,ddof=1)[0][1]/(σzp*σks)}\n\
Коэффициент Пирсона через np.corrcoef: {np.corrcoef(npzp,npks)[0][1]}')

import pandas as pd

df = pd.DataFrame({'zp': zp,
 'ks': ks})

pdcorr=df['zp']. corr(df['ks'])
print(f'4. Расчет коэффициента корреляции в pandas: {pdcorr}')