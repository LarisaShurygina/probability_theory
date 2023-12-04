# Когда используется критерий Стьюдента, а когда Z –критерий?

# Выбор критерия:
# Стьюдент: нормальность распределения; σ генеральной совокупности неизвестно; равенство дисперсий.
# Z-критерий: нормальное распределение; известно σ генеральной совокупности.


# 2. Проведите тест гипотезы. Утверждается, что шарики для подшипников, 
# изготовленные автоматическим станком, имеют средний диаметр 17 мм.
# Используя односторонний критерий с α=0,05, проверить эту гипотезу,
# если в выборке из n=100 шариков средний диаметр оказался равным 17.5 мм,
# а дисперсия известна и равна 4 кв. мм.

import math
import scipy.stats as stats

M0=17
Mn=17.5
n=100
D=4
σ=math.sqrt(D)

# Формулирование гипотез:
# H0 - гипотеза, что наблюдаемое выборочное среднее значение {Mn} попадает в генеральную совокупность со средним значением {M0}
# H1 - гипотеза, что наблюдаемое среднее больше среднего генеральной совокупности

α=0.05
print(f"Выбор уровня статистической значимости: Параметр α={α} задан условиями")

Zt=stats.norm.ppf(1-α)
print(f'Выбор статистического критерия:\n\
Предполагая нормальное распределение и известность σ={σ} генеральной совокупности, выбирается Z-критерий. Zt={Zt}')

Zn=(Mn-M0)/σ*math.sqrt(n)
print(f'Расчет наблюдаемого критерия: Zn=(Mn-M0)/σ*math.sqrt(n)={Zn}')

print(f'Сравнение табличного и наблюдаемого значения: Zt={Zt}, Zn={Zn}')

print(f'Вывод: Т.к. Zn > Zt, то гипотеза H0 отвергается. Т.е. наблюдаемое в выборке среднее значение диаметра не совпадает со средним \
диаметром в генеральной совокупности.')