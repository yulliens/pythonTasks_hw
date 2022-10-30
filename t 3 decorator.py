def info(fn):
   def wrapper(a, b):
      print(f'Данная функция выводит все числа между {a} и {b}, которые кратны трем')
      fn(a, b)
   return wrapper
@info
def ab_range(a, b):
   for i in range(a, b + 1):
      if i % 3 == 0:
          print(i)
ab_range(3, 7)
ab_range(13, 20)