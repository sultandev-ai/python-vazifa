#masala 1
# for i in range(1, 6):
#     for j in range(1,6):
#         print("*", end=" ")
#     print()


 # masala 2
# for i in range(1, 6):
#     print("#", end=" ")
#     for j in range(1,6):
#         print("*", end=" ")
#     print()

# masala 3
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1:
#             print("#", end=" ")
#         elif j == 1:
#             print("#", end=" ")
#         else:
#             print("*", end=" ")
#     print()

# masala 4

# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1:
#             print("#", end=" ")
#         elif j == 1:
#             print("#", end=" ")
#         elif j == 5:
#             print("#", end=" ")
#         else:
#             print("*", end=" ")
#     print()

#masala 5
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1:
#             print("#", end=" ")
#         elif j == 1:
#             print("#", end=" ")
#         elif i == 5:
#             print("#", end=" ")
#         elif j == 5:
#             print("#", end=" ")
#         else:
#             print("*", end=" ")
#     print()

#masala 6

# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1:
#             print("#", end=" ")
#         elif j == 1:
#             print("#", end=" ")
#         elif i == 5:
#             print("#", end=" ")
#         elif i == 3:
#             print("#", end=" ")
#         elif j == 5:
#             print("#", end=" ")
#         else:
#             print("*", end=" ")
#     print()

#masala 7
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1:
#             print("#", end=" ")
#         elif j == 1:
#             print("#", end=" ")
#         elif i == 5:
#             print("#", end=" ")
#         elif i == 3:
#             print("#", end=" ")
#         elif j == 5:
#             print("#", end=" ")
#         elif j == 3:
#             print("#", end=" ")
#         else:
#             print("0", end=" ")
#     print()

#masala 8

for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print("0",end=" ")
        else:
            print("*" ,end=" ")
    print()