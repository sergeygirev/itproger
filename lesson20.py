#function decorators
# import webbrowser
# def open_url(url):
#     webbrowser.open(url)
# open_url("http://google.com")

# import webbrowser
# def validator(func):
#     def wrapper(url):
#         if '.' in url:
#             func(url)
#         else:
#             print('Wrong URL')
#     return wrapper
# @validator
# def open_url(url):
#     webbrowser.open(url)
# open_url("http://google.com")

#homework from chatgpt
# def my_decorator(func):
#     def wrapper():
#         print('Start')
#         func()
#         print('End')
#     return wrapper
# @my_decorator
# def func():
#     print('Hello!')
# func()

# import time
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print('Took', round(end - start, 6), 'seconds')
#         return result
#     return wrapper
# @timer
# def func():
#     total = 0
#     for i in range(1_000_000):
#         total += i
#     return total
# res = func()
# print('Total', res)