#1
# k = int(input("k = "))
# n = int(input("n = "))
# for i in range(n):
#     print(k)

#2
# a = int(input("a = "))
# b = int(input("b = "))
# s = 0
# for i in range(a, b+1):
#     print(i)
#     s += 1
# print("Soni =", s)

#3
# a = int(input("a = "))
# b = int(input("b = "))
# s = 0
# for i in range(b, a-1, -1):
#     print(i)
#     s += 1
# print("Soni =", s)

#4
# narx = float(input("narx = "))
# for i in range(1, 11):
#     print(i, "kg =", i * narx)

#5
# narx = float(input("narx = "))
# for i in range(1, 10):
#     print(i/10, "kg =", (i/10) * narx)

#6
# narx = float(input("narx = "))
# j = 1.0
# while j <= 2.0:
#     print(j, "kg =", j * narx)
#     j += 0.2

#7
# a = int(input("a = "))
# b = int(input("b = "))
# S = 0
# for i in range(a, b+1):
#     S += i
# print(S)

#8
# a = int(input("a = "))
# b = int(input("b = "))
# S = 1
# for i in range(a, b+1):
#     S *= i
# print(S)

#9
# a = int(input("a = "))
# b = int(input("b = "))
# S = 0
# for i in range(a, b+1):
#     S += i*i
# print(S)

#10
# n = int(input("n = "))
# S = 0
# for i in range(1, n+1):
#     S += 1 / i
# print(S)

#11
# n = int(input("n = "))
# S = 0
# for i in range(1, n+1):
#     S += (n+i)*(n+i)
# print(S)

#12
# n = int(input("n = "))
# S = 1
# for i in range(1, n+1):
#     S *= (1 + i/10)
# print(S)

#13
# n = int(input("n = "))
# S = 0
# ishora = 1
# for i in range(1, n+1):
#     S += ishora * (1 + i/10)
#     ishora *= -1
# print(S)

#14
# n = int(input("n = "))
# S = 0
# son = 1
# for i in range(n):
#     S += son*son
#     son += 2
# print(S)

#15
# n = int(input("n = "))
# a = float(input("a = "))
# nat = 1
# for i in range(n):
#     nat *= a
# print(nat)

#16
# n = int(input("n = "))
# a = float(input("a = "))
# for i in range(1, n+1):
#     print(i, "daraja =", a**i)

#17
# n = int(input("n = "))
# a = float(input("a = "))
# S = 0
# for i in range(1, n+1):
#     S += a**i
# print(S)

#18
# n = int(input("n = "))
# a = float(input("a = "))
# S = 0
# ishora = 1
# for i in range(1, n+1):
#     S += ishora * (a**i)
#     ishora *= -1
# print(S)

#19
# n = int(input("n = "))
# S = 1
# for i in range(1, n+1):
#     S *= i
# print(S)

#20
n = int(input("n = "))
S = 0
for i in range(1, n+1):
    f = 1
    for j in range(1, i+1):
        f *= j
    S += f
print(S)
