import random 
print("Генератор рассказов средневековья")
hero=['Magican','Elf','Warrioir','Huntsman']
action=['Kills','Helps']
enviorment=['people','animals','villians','royal guardians']
rnd1= (random.choice(hero))
rnd2=(random.choice(action))
rnd3= (random.choice(enviorment))
fullrandom=f"{rnd1} {rnd2} {rnd3}"
print(fullrandom)
t=str("""Если бы в следующее утро Степе Лиходееву сказали бы так: «Степа! Тебя расстреляют, если ты сию минуту не встанешь!» – Степа ответил бы томным, чуть слышным голосом: «Расстреливайте, делайте со мною, что хотите, но я не встану».""")
a=len(t)
print ("Отсутвует пробел>>",a)
t=str("""Если бы в следующее утро Степе Лиходееву сказали бы так: «Степа! Тебя расстреляют, если ты сию минуту не встанешь!» – Степа ответил бы томным, чуть слышным голосом: «Расстреливайте, делайте со мною, что хотите, но я не встану».""").split(' ')
b=len(t) 
b= a-b
print ("Присутствует пробел>> ", b )
t=str("""Если бы в следующее утро Степе Лиходееву сказали бы так: «Степа! Тебя расстреляют, если ты сию минуту не встанешь!» – Степа ответил бы томным, чуть слышным голосом: «Расстреливайте, делайте со мною, что хотите, но я не встану».""").split(' ')
a=len(t)
print ("Количество слов>>", a)