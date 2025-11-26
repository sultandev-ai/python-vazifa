uzunlik = int(input("uzunllikni kiriting (s) :"))
metr = uzunlik / 100
print(f" metrda : {metr} ")



m = int(input("kg ni kiriting (kg) :"))
ton = m / 1000
print(f" {ton} tonna boladi ")



bayt = int(input(" baytalarni kiriting :"))
kilo = bayt // 1024
print(f" {kilo} kb boladi ")



son1 = int(input(" A sonini kiriting : "))
son2 = int(input(" B sonini kiriting : "))
natija = son1 // son2
print(f" {natija} marta ")



son1 = int(input(" A sonini kiriting : "))
son2 = int(input(" B sonini kiriting : "))
natija = son1 % son2
print(f" {natija} marta ")



son = int(input("ikki xonali son kiriting :"))
birlik = son % 10
onlik = son // 10
print(f" birlik : {birlik} ")
print(f"  onlik : {onlik} ")



son = int(input("ikki xonali son kiriting :"))
birlik = son % 10
onlik = son // 10
res = birlik + onlik
print(f" yigindi  : {res} ")



son = int(input("ikki xonali son kiriting :"))
birlik = son % 10
onlik = son // 10
print(f" nstija  : {birlik}{onlik} ")



son = int(input("uch xonali son kiriting :"))
birlik = son % 10
onlik = son // 10 % 10
yuzlik = son // 100 % 10
print(f" nstija  : {yuzlik} ")


son = int(input("uch xonali son kiriting :"))
birlik = son % 10
onlik = son // 10 % 10
yuzlik = son // 100 % 10
print(f" birlik  : {birlik}  ")
print(f" onlik  : {onlik}  ")


son = int(input("uch xonali son kiriting :"))
birlik = son % 10
onlik = son // 10 % 10
yuzlik = son // 100 % 10
natija = birlik + yuzlik + onlik
print(f" nstija  : {natija} ")


son = int(input("uch xonali son kiriting :"))
birlik = son % 10
onlik = son // 10 % 10
yuzlik = son // 100 % 10
print(f" natija : {birlik}{onlik}{yuzlik} ")


son = int(input("3 xonali sonni kiriting :"))
yuzlik = son // 100
qoldiq = son % 100
yangison = (qoldiq * 10) + yuzlik
print(f" natija : {yangison}")


son = int(input("3 xonali sonni kiriting :"))
yuzlik = son % 10
qoldiq = son // 10
yangison = (yuzlik * 10) + qoldiq
print(f" natija : {yangison}")



a = int(input(" a : "))
b = int(input(" b : "))
res = a > b
print(res)

a = int(input("son :"))
birlik = a % 10
onlik = a // 10

res = birlik != onlik
print(res)
