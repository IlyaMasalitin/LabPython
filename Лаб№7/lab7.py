#Задание 1 21 вариант
from numpy import *
import matplotlib.pyplot as plt
from collections import Counter
import re
x = linspace(1, 4, 100)
y = 5*sin(1/x)*cos(x**2+1/x)**2
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
#Задание 2
with open ('sobachie serdce.txt', 'r', encoding='utf-8') as f:
    for i in f:
        text = i
    chars = " !#$%&'()*+,-./:;<=>?@^_`{|}~–«»"
    for x in chars:
        if x in i:
            text = text.replace(x, '')
c = Counter(text)
plt.bar(*zip(*c.most_common()), width=0.2, color='red')
plt.show()
#Задание 3
with open('sobachie serdce.txt', 'r', encoding = 'utf-8') as f:
    for i in f:
        text = i
        chars = re.compile(r"\.\.\.|\.|\!|\?")
        c = Counter(chars.findall(text))
plt.bar(*zip(*c.most_common()), width=0.5, color='green')
plt.show()