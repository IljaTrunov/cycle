#5
S=int(input("Хочешь вычислить трапецию (Равнобедренную)? 1-Да 2-Нет"))
if S==1:
    a=0.0
    while type(a)!=int and a<=0:
        try:
            a=int(input("A= "))
        except ValueError:
            print("Только цифры")
    b=0.0
    while type(b)!=int and b<=0:
        try:
            b=int(input("B= "))
        except ValueError:
            print("Только цифры")
    h=0.0
    while type(h)!=int and h<=0:
        try:
            h=int(input("H= "))
        except ValueError:
            print("Только цифры")
    S=0.5*(a+b)*h
    print("Площадь: ",S)
    q=input("Ты закончил?")
    if q!="Да" or "да": quit()
elif S==2:
    print("А, ну ок, пока")

    

#4
from random import *
M=randit(100,1000)
print("Meie on kang:",M,"m")
while M>0:
    M=int(input("Mitu meetri tahad osta?"))
    if M<m:
        m-=M
        print("Meil on jäänud: ",M,"m")
    else:
        v=input("Kas tahad jääk osta?")
        if v=="jah":
            print("Kang on teie oma!")
            M=0
        else:
            print("Ei taha, siis ei taha!")
print("Pood on tühi!", M)

km=s_pikkus=10
print("1. esimesel päeval pikkus oli ",km)
print("terve tee pikkus oli ",round(s_pikkus,2))
for d in range(2,8):
    km*=1.1
    print(". päeval pikkus oli ",round(km,2))
    s_pikkus+=km
    print("terve tee pikkus oli ",round(s_pikkus,2))
    #3
   

ask_p=ask_n=""
while type(ask_p)!=int:
    try:
        ask_p=int(input("Сколько чисел ты хочешь ввести? "))
    except ValueError:
        print("Только цифры")

if ask_p>0:
    while type(ask_p)!=int:
    try:
        ask_p=int(input("Какое число ты хочешь написать? "))
    except ValueError:
        print("Только цифры")
        ask_n=int(input("Цифра"))
        ask_p-=1
        max=ask_n
    while ask_p>0:
        while type(ask_n)!=int:
     try:
        ask_p=int(input("Сколько чисел ты хочешь ввести? "))
    except ValueError:
        print("Только цифры")
        ask_n=int(input("Цифра"))
        ask_p-=1
if ask_n>max: max=ask_n
     print("Максимальное число найдено")
else:
     print("не найдено максимальное число")
 #1
t=0 #количество чисел
q=0 #int
while t<1:
    t+=1
    a=float(input("sisesta arv:"))
    if a==round(a): q+=1
print("Täisarvude kogus:",q)
#1
t=0
q=0
for t in range(1):
    a=float(input("sisesta arv:"))
    if a==round(a): q+=1
print("Täisarvude kogus:",q)
#2
A=4
s=0
for arv in range(1,a+1):
    s+=arv
print("Summa:",s)

#3
from random import *
korrutis=1
for i in range(8):
    B=randint(-100,100)
    print(B)
    if B>0: korrutis*=B
print("Korrutis on",korrutis)
#4
for a in range(10,20):
    print(a**2)
#6
p=0
from random import *
N=int(input("Mitu: "))
p=n=o=0
while N>0:
    N-=1
    B=randint(-100,100)
    print(B)
    if B>0:
        p+=1
    elif B<0:
        n+=1
    else:
        o+=1
print("Pos:",p)
print("Neg:",n)
print("Nul:",0)
#Задача:Купи слона!
loom=input("Купи слона")
while loom.title()!="Слон":
    loom=input("Все говорят"+loom+"!А ты купи!!!")
 # Домашнее задание (на выбор)
    #9
p=3
n=float(input('Кол-во лет: '))
s=float(input('Сумма на счету: '))
 
for i in range(int(n)):
    s+=s*(p/100)
print(f"Через {int(n)} лет у тебя будет аж {s}, хватит на свидание и подарить агапчику билет в шашлычную.")
#.
a=int(input("Sisesta arv: "))
for i in range(1,10):
    print(Z,"*",i,"=",Z*i)
#15
for g in range(0,10,1):
    for i in range(0,10,1):
        print(i,end=" ")
# Таблица умножения
for g in range(0,10):
  for i in range(0,10):
      print(f"{(g*i):2}",end=" ")
print()
#16
n=int(input("Введите число для столбика: "))
for i in range(1, 11):
    print(f"{i}*{n}={i*n}")
#16
for g in range(0,10,1):
    for i in range(0,10,1):
        if i==g:
            print(i,end=" ")
        else:
            print("0",end=" ")
#28
import random
print("Привет, давай сыграем в игру! Набери число от 0 до 20. Посмотрим, угадаешь ли ты число или нет.")
errors=0
rand=random.randint(0, 20) 
while errors<6:
    number=input()
    if number.isdigit():
        number=int(number)
        if number<rand:
            print("Напиши число побольше")
        elif number>rand:
            print("Напиши число поменьше")
        else:
            print(f"Красавчик... число было: {rand}!")
            break
        errors += 1
    else:
        print("Ты как бы не то ввел))")
else:
    print(f"Число было: {rand}, не фортануло, еще раз пробуй!")





print("FOR".center(60,"$"))
for i in range(5):
    print("Hello world!!!")
print("WHILE TRUE")
k=0
while True:
    k+=1
    print("Hello world!!!")
    if k==5: break
print("WHILE Tingimusega")
k=0
while k<5:
    print("Hello world!!!")
    k+=1
