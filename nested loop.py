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
for i in range(1, 6):
    for j in range(1, 6):
        if i == 1:
            print("#", end=" ")
        elif j == 1:
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()
