# a = int(input())
# b = int(input())
# c = a
# print(f'Before:\na = {a}\nb = {b}')
# a = b
# b = c
# print(f'After:\na = {a}\nb = {b}')

a = int(input())
b = int(input())
print(f'Before:\na = {a}\nb = {b}')
b, a = a, b
print(f'After:\na = {a}\nb = {b}')