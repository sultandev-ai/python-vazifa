# 1
# a = int(input("a = "))
# if a > 0:
#     a = a + 1
# print(a)
#
# 2
# a = int(input("a = "))
# if a > 0:
#     a = a + 1
# else:
#     a = a - 2
# print(a)
#
# 3
# a = int(input("a = "))
# if a > 0:
#     a = a + 1
# elif a < 0:
#     a = a - 2
# else:
#     a = 10
# print(a)
#
# 4
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# cnt = 0
# if a > 0: cnt += 1
# if b > 0: cnt += 1
# if c > 0: cnt += 1
# print(cnt)
#
# 5
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# pos = 0
# neg = 0
# if a > 0: pos += 1
# elif a < 0: neg += 1
# if b > 0: pos += 1
# elif b < 0: neg += 1
# if c > 0: pos += 1
# elif c < 0: neg += 1
# print(pos, neg)
#
# 6
# a = int(input("a = "))
# b = int(input("b = "))
# if a > b:
#     print(a)
# else:
#     print(b)
#
# 7
# a = int(input("a = "))
# b = int(input("b = "))
# if a < b:
#     print(1)
# else:
#     print(2)
#
# 8
# a = int(input("a = "))
# b = int(input("b = "))
# if a > b:
#     print(a, b)
# else:
#     print(b, a)
# 9
# a = float(input("a = "))
# b = float(input("b = "))
# if a > b:
#     a, b = b, a
# print(a, b)
#
# 10
# a = int(input("a = "))
# b = int(input("b = "))
# if a != b:
#     s = a + b
#     a = s
#     b = s
# else:
#     a = 0
#     b = 0
# print(a, b)
#
# 11
# a = int(input("a = "))
# b = int(input("b = "))
# if a != b:
#     m = max(a, b)
#     a = m
#     b = m
# else:
#     a = 0
#     b = 0
# print(a, b)
#
# 12
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# print(min(a, b, c))
#
# 13
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# mx = max(a,b,c)
# mn = min(a,b,c)
# print(a + b + c - mx - mn)
#
# 14
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# print(min(a,b,c), max(a,b,c))
#
# 15
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# ab = a + b
# ac = a + c
# bc = b + c
# print(max(ab, ac, bc))
#
# 16
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# if a < b < c:
#     a *= 2
#     b *= 2
#     c *= 2
# else:
#     a = -a
#     b = -b
#     c = -c
# print(a, b, c)
#
# 17
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# if (a < b < c) or (a > b > c):
#     a *= 2
#     b *= 2
#     c *= 2
# else:
#     a = -a
#     b = -b
#     c = -c
# print(a, b, c)
#
# 18
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a == b:
#     print(3)
# elif a == c:
#     print(2)
# else:
#     print(1)
#
# 19
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# d = int(input("d = "))
# if a == b == c:
#     print(4)
# elif a == b == d:
#     print(3)
# elif a == c == d:
#     print(2)
# else:
#     print(1)
#
# 20
# a = int(input("A = "))
# b = int(input("B = "))
# c = int(input("C = "))
# d_ab = abs(a - b)
# d_ac = abs(a - c)
# if d_ab < d_ac:
#     print("B", d_ab)
# else:
#     print("C", d_ac)
#
# 21
# x = int(input("x = "))
# y = int(input("y = "))
# if x == 0 and y == 0:
#     print(0)
# elif x == 0:
#     print(2)
# elif y == 0:
#     print(1)
# else:
#     print(3)
#
# 22
# x = int(input("x = "))
# y = int(input("y = "))
# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# else:
#     print(4)
# 23
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
x3 = int(input("x3 = "))
y3 = int(input("y3 = "))
if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
else:
    x4 = x1
if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
else:
    y4 = y1
print(x4, y4)