#1
# A = int(input("A = "))
# B = int(input("B = "))
# s = 0
# q = A
# while q >= B:
#     q -= B
#     s += 1
# print(s, q)

#2
# A = int(input("A = "))
# B = int(input("B = "))
# s = 0
# q = A
# while q >= B:
#     q -= B
#     s += 1
# print(s)

#3
# N = int(input("N = "))
# K = int(input("K = "))
# qoldiq = N
# butun = 0
# while qoldiq >= K:
#     qoldiq -= K
#     butun += 1
# print(butun, qoldiq)

#4
# n = int(input("n = "))
# x = n
# while x > 1:
#     x -= 3
# if x == 1:
#     print("3 ning darajasi")
# else:
#     print("3 ning darajasi emas")

#5
# n = int(input("n = "))
# k = 0
# son = 1
# while son < n:
#     son *= 2
#     k += 1
# print(k)

#6
# n = int(input("n = "))
# S = 1
# x = n
# while x > 1:
#     S *= (x * (x - 2))
#     x -= 4
# print(S)

#7
# n = int(input("n = "))
# k = 1
# while k*k <= n:
#     k += 1
# print(k)

#8
# n = int(input("n = "))
# k = 1
# while (k+1)*(k+1) <= n:
#     k += 1
# print(k)

#9
# n = int(input("n = "))
# k = 0
# son = 1
# while son <= n:
#     son *= 3
#     k += 1
# print(k)

#10
n = int(input("n = "))
k = 0
son = 1
while son * 3 <= n:
    son *= 3
    k += 1
print(k)
