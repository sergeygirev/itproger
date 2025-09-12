# functions (`def`, `lambda`)
# def test_func():
#     print("hello", end="")
#     print("!")
# test_func()

# def test_func(word):
#     print(word, end="")
#     print("!")
# test_func('hello')
# test_func(5)

# def summ(a, b):
#     res = a + b
#     print('Result:', res)
# summ(5, 7)
# summ('H','i')

# def summ(a, b):
#     # res = a + b
#     # return res
#     return a + b
# res = summ(5, 7)
# print(res)
# print(summ('H','i'))

# def minimal(l):
#     min_number = l[0]
#     for el in l:
#         if el < min_number:
#             min_number = el
#     return min_number
#
# nums1 = [5,7,2,4,9]
# min = nums1[0]
# for el in nums1:
#     if el < min:
#         min = el
# print(min)
# min1 = minimal(nums1)
#
# nums2 = [5.4,7.5,2.3,2.1,4,9]
# min2 = nums2[0]
# for el in nums2:
#     if el < min2:
#         min2 = el
# print(min2)
# min2 = minimal(nums2)

# if nums1 < nums2:
#     print(min1)
# else:
#     print(min2)

# func = lambda x, y: x * y
# res = func(1, 2)
# print(res)

#homework from chatgpt

# def square(x):
#     return x*x
# print(square(5))

# def sum_print(a, b):
#     print(a + b)
# def sum_return(a, b):
#     return a + b
# print(sum_print(3, 4 + 10))
# print(sum_return(5, 4 + 10))

# def calc(a,b, c):
#     return (a+b)*c
# print(calc(2,3,4))