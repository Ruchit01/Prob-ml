# l = input("Enter the string here: ")
# def helper(s: str, help_string: str, k: int):
#     if k == len(s):
#         return help_string
#     if help_string == "":
#         help_string = help_string + s[0] + "1"
#     else:
#         if s[k] == help_string[-2]:
#             help_string = help_string[:-1] + str(int(help_string[-1])+1)
#         else:
#             help_string = help_string + s[k] + "1"
#     k+=1
#     return helper(s, help_string, k)

# def string_compressor(string):
#     compressed_string = helper(string, help_string="", k=0)
#     return compressed_string

# print(string_compressor(l))

# def safe_calculate(a: float, b: float, operator: str) -> float:
#     assert type(a) == float and type(b) == float, "Operands must be numeric."
#     if operator == "+":
#         print(a+b)
#         return "Operation complete"
#     elif operator == "-":
#         print(a-b)
#         return "Operation complete"
#     elif operator == "*":
#         print(a*b)
#         return "Operation complete"
#     else:
#         try:
#             if operator == "/":
#                 return a/b
#         except ZeroDivisionError as z:
#             print("ZeroDivisionError: Cannot divide by zero")
#             return None
#         else:
#             print("ValueError: Unsupported operator")
#             return None
#         finally:
#             print("Operation complete")

# def solution(tc):
#     a, b, op = tc
#     return safe_calculate(a, b, op)


# def process_input(filename):
#     lines = open(filename, 'r').readlines()
#     lines = [line.strip() for line in lines]
#     num_tests = int(lines[0])
#     input_tests = []
#     for line in lines[1:num_tests + 1]:
#         parts = line.split()
#         a_str, b_str, operator = parts

#         try:
#             a = float(a_str)
#         except ValueError:
#             a = a_str

#         try:
#             b = float(b_str)
#         except ValueError:
#             b = b_str

#         input_tests.append((a, b, operator))
#     return input_tests


# if __name__ == "__main__":
#     Input = process_input("p3_input.txt")
#     for tc in Input:
#         result = solution(tc)
#         if result is not None:
#             print(result)

'''
list of lists -> [[-1,2,3], [4,0,-5], [10,-9,8]] :
    Remove negative numbers
    Double positive numbers
    Flatten the list
'''
# final_list = []
# def list_appender(lst):
#     global final_list
#     for i in range(len(lst)):
#         final_list.append(lst[i])
#     pass

# def filt_func(lst):
#     filtered_list = list(filter(lambda x: x>=0, lst))
#     filtered_list = list(map(lambda x: 2*x, filtered_list))
#     return filtered_list

# def func(lst):
#     mapped_lst = list(map(filt_func, lst))
#     return mapped_lst

# def final(lst):
#     final_list = list(map(list_appender, lst))


# l = [[-1,2,3], [4,0,-5], [10,-9,8]]
# final(func(l))
# print(final_list)


# test_cases = int(input())
# Array1 = []
# for i in range(test_cases):
#     n = input()
#     n = int(n)
#     l = input().split()
#     l = list(map(int, l))
#     Array1.append(l)

# def positive_maker(lst: list):
#     n = lst.count(0)
#     m = lst.count(-1)
#     if m%2 == 0:
#         return n
#     else:
#         return n + 2
# for i in range(test_cases):
#     print(positive_maker(Array1[i]))

# l1 = [1,2]
# l2 = l1[:len(l1)//2]
# print(l2)
a = "hello"
b = "hi"
if b != a:
    raise ValueError("Error")