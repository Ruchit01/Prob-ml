# L = ["a", "b" , "c", " "]
# M = []
# sub = []
# def f(x):
#     a = x 
#     if a == []:
#         return
#     if a in M:
#         return
#     if a not in M:
#         M.append(a)
#         print(a)
#         sub.append(a)
#     for i in range(len(a)):
#         y = a[0:i] + a[i+1: len(a)]
#         f(y)
# f(L)
# k = []
# for i in sub:
#     if len(i)== 3:
#         k.append(i)
# print(k)


# def power_print(n):
#     global k
#     if 3**(k+1) > n:
#         return 
#     k+=1
#     print(3**k)
#     power_print(n)

# n = int(input("Enter the number: "))
# k = -1
# power_print(n)


# def hanoi(n):
#     if n==2:
#         return 3
#     return 2**(n-1) + hanoi(n-1) 

# n = int(input("Enter the value of n: "))
# print(hanoi(n))


# def sum1(lst):
#     if len(lst) == 1:
#         return lst[0]
#     return lst[0] + sum1(lst[1:])

# l = input("Enter elements of list: ").split()
# l = list(map(int, l))
# print(sum1(l))


# def permutation(l):

#     pass
# l = "abcd"
# lst = []
# for i in l:
#     lst.append(i)

# def square(n):
#     return n*n

# def apply_n_times(value, func, n=1):
#     if n == 1:
#         return func(value)
#     elif n==0:
#         return value
#     elif n>1:
#         return apply_n_times(func(value), func, n-1)

# print(apply_n_times(5, square, 2))

# n_cases = int(input())
# arr = []
# k_input = []
# days = []
# for i in range(n_cases):
#     a,b = input().split()
#     d = input().split()
#     a = int(a)
#     b = int(b)
#     days.append(d)
#     arr.append(a)
#     k_input.append(b)

# def max_rides(days: list, k: int)-> int:
#     count = 0
#     n = len(days)
#     i = 0
#     while i + k <= n:
#         if all(days[j] == '0' for j in range(i,i+k)):
#             count+=1
#             i+=k+1
#         else:
#             i+=1
#     return count
    
# for i in range(n_cases):
#     print(max_rides(days[i], k_input[i]))

# n_cases = int(input())
# l = []
# for i in range(n_cases):
#     n = input()
#     l.append(n)
# for j in l:
#     k = j[0]
#     for i in range(1, len(j)):
#         if j[i] < k:
#             k = j[i]
#     print(k)


