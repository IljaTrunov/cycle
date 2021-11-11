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
 # Домашнее задание (на выбор?)
    #9
n=float(input('Кол-во лет: '))
p=3
s=float(input('Сумма на счету: '))
 
for i in range(int(n)):
    s += s * (p/100)
print(f"Через {int(n)} лет у тебя будет аж {s}, хватит на свидание и подарить агапчику билет в шашлычную.")





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
