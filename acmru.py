# def is_kabissa(year):
#     if year % 400 == 0:
#         return True
#     if year % 100 == 0:
#         return False
#     if year % 4 == 0:
#         return True
#     return False

# year = int(input())
# kabissa = is_kabissa(year)

# if kabissa:
#     print(f'12/09/{year}')
# else:
#     print(f'13/09/{year}')

# n, s = map(str, input().strip().split())
# index = int(n)-1
# print(s[:index]+s[index+1:])

# n = int(input())
# s = 0
# for i in range(1, 1+n):
#   if n%i==0:
#     s+=i
# print(s)

# n = int(input())
# ls = list(map(int, input().split()))
# s = 0
# for i in ls:
#     s+=(i-1)
# print(s+1)

# a=int(input()) 
# if a%2==1: 
#     print(a) 
# if a%2==0: 
#     print(a//2)
# k = int(input()) 
# s = 0 
# for i in range(1, k + 1): 
#     s += i 
#     if s > k: 
#         print(i - 1) 
#         break 
#     elif s == k: 
#         print(i)
#         break

# from math import pi, sqrt
# S , r1 = map(float, input().split())
# r2 = sqrt((pi*r1**2 - S)/pi)
# print('{:.3f}'.format(r2))

n = int(input())
ls = []
if n-1>=1:
    ls.append(n - 1)
if (n+1)<=64:
    ls.append(n+1)
if n-8>=1:
    ls.append(n - 8)
if (n + 8)<=64:
    ls.append(n+8)
ls.sort()
for i in ls:
    print(i, end=' ')
ls = []
if (n + 8 > 64) :
    ls.append(n - 8)
if (n % 8 - 1 > 0 or n % 8 - 1 == -1):
    ls.append(n - 1)
if (n % 8 != 0 and n % 8 + 1 <= 8) :
    ls.append(n + 1)
if (n - 8 < 1) :
    if (n % 8 - 1 > 0 or n % 8 - 1 == -1) :
        ls.append(n - 1 )
    if (n % 8 != 0 and n% 8 + 1 <= 8) :
        ls.append(n + 1 )
    ls.append(n + 8)
print(ls)