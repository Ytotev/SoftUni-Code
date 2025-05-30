# https://pyseek.com/2022/02/learn-25-important-pattern-programs-in-python/
# n = 6
# for row in range(n):
#     for row_element in range(n +2):
#         print("*", end=" ")
#     print()

# Triangle
# n = 9
# for i in range(n):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(n - i -1):
#         print(" ", end=" ")
#     for j in range(2 * i + 1):
#         print("*", end=" ")
# #     print()
#
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

number_list = [1, 2, 3, 5, 4, 3]

number_list.remove(3)
number_list.remove(4)

print(number_list)

