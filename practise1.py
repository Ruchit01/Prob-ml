

# A = [1,5,3,7,84,2,4,5,7,34,23,21,31]
# print(divide_lst(A))
# def lcm(a,b):
#     if max(a,b)%min(a,b)==0:
#         return max(a,b)
#     else:
#         return a*b


# def ans(A,B,C):
#     l_a = []
#     l_b = []
#     for i in range(1,C+1):
#         l_a.append(A*i)
#         l_b.append(B*i)
#     final_lst = merge(l_a,l_b)
#     print(final_lst)
#     x = final_lst[C-1]
#     if not(x%A and x%B) :
#         k = x
#         lcm_ = lcm(A,B)
#         while (k>=0):
#             print(k, end=" ")
#             k -= lcm_
#     elif x%A == 0 and x%B:
#         k = x
#         while (k>0):
#             print(k, end=" ")
#             k -= A
#     elif x%B == 0 and x%A:
#         k = x
#         while (k>0):
#             print(k, end=" ")
#             k -= B

# ans(3,5,14)




# lst = input("Enter the elements of the list: ").split()
# lst = list(map(int, lst))
# n = int(input("Enter the value of k: "))

# def func(arr, k):
    # cnt = [0] * k
    # for x in arr:
    #     cnt[x % k] += 1

    # ans = 0

    # # remainder 0: take at most one
    # if cnt[0] > 0:
    #     ans += 1

    # # handle 1..k//2
    # # if k even, we will treat k/2 specially
    # limit = k // 2

    # for r in range(1, limit + 1):
    #     if r == k - r:       # this only happens when k is even and r == k/2
    #         # take at most one from this remainder class
    #         if cnt[r] > 0:
    #             ans += 1
    #     else:
    #         ans += max(cnt[r], cnt[k - r])

    # return ans


# print(func(lst, n))

# n = int(input())
# k = []
# for i in range(n):
#     k_i = int(input())
#     k.append(k_i)



# def config(n):
#     if n<=0:
#         return 0
#     elif n%2 == 1:
#         return 0
#     elif n==2:
#         return 1
#     elif n == 4:
#         return 2
#     p1 = config(n-2)
#     p2 = config(n-4)
#     return p1+p2

# for i in range(n):
#     print(config(k[i]))


# def f(A, B):
#     if A[-1]>B[-1]:
#         count = len(B)
#     else:
#         return f(A, B[:-1])

# n = int(input())
# strings = []
# for i in range(n):
#     n1 = int(input())
#     k = input()
#     strings.append(k)

# def difference(s: str) -> int:
#     count = 0
#     s = s[::-1]
#     for i in s:
#         if i != s[0]:
#             i = s[0]
#             count += 1
#     return count

# for i in range(n):
#     print(difference(strings[i]))  


# test_num = int(input())
# num = []
# for i in range(test_num):
#     k = int(input())
#     num.append(k)

# def farm(n):
#     chicken = []
#     cow = []
#     count = 0
#     for i in range(0,n//2 + 1):
#         for j in range(0,n//4 + 1):
#             if i not in chicken and j not in cow:
#                 if 2*i + 4*j == n:
#                     count += 1
#                     chicken.append(i)
#                     cow.append(j)
#     return count

# for i in range(test_num):
#     print(farm(num[i]))


# test_num = int(input())
# lst = []
# for i in range(test_num):
#     k = int(input())
#     l = input().split()
#     l = list(map(int, l))
#     lst.append(l)
# def arr_bal(l):
#     c = 0
#     l2 = []
#     for i in l:
#         if i not in l2:
#             l2.append(i)
#     print(l2)
#     for i in l2:
#         k = l.count(i)
#         if i == 0:
#             c += k
#         elif  k!= i:
#             if k < i:
#                 c += k
#             elif k > i:
#                 c += k - i
#     return c

# for i in range(test_num):
#     print(arr_bal(lst[i]))

# test_num = int(input())
# lst_s = []
# lst_k = []
# for i in range(test_num):
#     n,k = input().split()
#     k = int(k)
#     lst_k.append(k)
#     s = input()
#     lst_s.append(s)
# def sleep_count(s,k):
#     i = 0
#     sleep = 0
#     while i < len(s):
#         if s[i] == "1":
#             h = 0
#             for j in range(1,k+1):
#                 if i+j < len(s) and s[i+j] == "1":
#                     i += j
#                     h=1
#             if h == 0:
#                  i += k+1

#         elif s[i] == "0":
#             sleep += 1
#             i += 1
#     return sleep
# print(sleep_count("1001", 1))

# for i in range(test_num):
#     print(sleep_count(lst_s[i], lst_k[i]))

# merged_lst = []
# def merge(l1, l2):
#     global merged_lst
#     if l1 == []:
#         return l2
#     elif l2 == []:
#         return l1
#     if l1[0]<l2[0]:
#         return [l1[0]] + merge(l1[1:], l2)
#     elif l1[0] == l2[0]:
#         return [l1[0]] + merge(l1[1:], l2[1:])
#     else:
#         return [l2[0]] + merge(l1, l2[1:])
    
# def divide_lst(lst):
#     mid = len(lst)//2
#     if len(lst)<= 1:
#         return lst
#     l1 = divide_lst(lst[:mid])
#     l2 = divide_lst(lst[mid:])
#     return merge(l1, l2)

t = int(input())
N = []
LST = []
for i in range(t):
    n = int(input())
    lst = input().split()
    lst = list(map(int, lst))
    # print(lst)
    N.append(n)
    LST.append(lst)

def mex(arr):
    arr.sort()
    m = 0
    for i in arr:
        if (m == i): 
            m += 1
    return m
        

def func(n, a):
    a.sort()
    for i in range(1, n):
        left = a[:i]
        # print(left)
        right = a[i:]
        # print(right)
        mex_left = mex(left)
        mex_right = mex(right)
        # print(mex_left, mex_right)
        if mex_left == mex_right:
            return "NO"
    return "YES"

for i in range(t):
    print(func(N[i], LST[i]))
    
# print(mex([3, 0]))