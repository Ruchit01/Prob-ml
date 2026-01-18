# import pdb
# pdb.set_trace()


# def rev(s):
#     l = len(s)
#     if l == 1:
#         return s[0]
#     return s[l-1]+ rev(s[0:l-1])
# s = input("Enter the string: ")
# print(rev(s))



# def pal(x):
#     global s
#     x = x.lower()
#     if x == "":
#         return "Yes it is a palindrome"
#     if x[0]== x[-1]:
#         return pal(x[1:-1])
#     else:
#         return "Not a palindrome"

# s = input("Enter the string here: ")

# print(pal(s))

# k = 0
# def counter(n):
#     global k
#     if n =="":
#         return ""
#     k+=1
#     return counter(n[0:-1])

# n = input("Enter the number: ")
# counter(n)
# print(k)

# def counter(n,m):
#     if (n,m) == (1,1):
#         return 1
#     elif n==1 or m==1:
#         return 1
#     return counter(n-1,m) + counter(n,m-1)

# n = int(input("Enter the value of n: "))
# m = int(input("Enter the value of m: "))
# print(counter(n,m))

# def list_sum(l):
#     if l == []:
#         return 0
#     return l[-1] + list_sum(l[0:-1])

# lst = input("Enter the elements of the list separated with spaces: ").split()
# lst = list(map(int, lst))
# print(list_sum(lst))


# n = 0
# def max(l):
#     global n
#     if l == []:
#         return n
#     elif l[0]>n:
#         n = l[0]
#     return max(l[1:])

# lst = input("Enter the elements of the list separated with spaces: ").split()
# lst = list(map(int, lst))
# print(max(lst))

# def find(l, m):
#     if l == []:
#         return 0
#     return 1 + find(l[1:],m) if l[0] == m else find(l[1:], m)
#     pass

# lst = input("Enter the elements of the list separated with spaces: ").split()
# lst = list(map(int, lst))
# n = int(input("Enter the number you want to find: "))
# print(find(lst, n))


# def find(l, m):
#     l1 = len(l)
#     if l == []:
#         return False
#     mid = l1//2
#     if m == l[mid]:
#         return True
#     elif m > l[mid]:
#         return find(l[mid+1:], m)
#     else:
#         return find(l[:mid], m)

# lst = input("Enter the elements of the list separated with spaces: ").split()
# lst = list(map(int, lst))
# n = int(input("Enter the number you want to find: "))
# print(find(lst, n))

# k = []
# def f(lst):
#     global k
#     l = len(lst)



# j = [1,[2,[3,[4],[10],5],[12,[56],[1],8],6],9]
# f(j)
# print(k)

# def hanoi(n):
#     if n==2:
#         return 3
#     return 2**(n-1) + hanoi(n-1) 

# n = int(input("Enter the value of n: "))
# print(hanoi(n))

# l = []
# def pascal(n):
#     l1 = []
#     if n == 1:
#         print([1])
#         return
#     elif n == 2:
#         print([1,1])
#         return
#     else:
#         l.append(1)
#         for i in range():
#             pass

# n = int(input("Enter the value of n: "))
# pascal(n)
# print(l)




