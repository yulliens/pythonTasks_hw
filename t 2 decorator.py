def add_new(fn):
   def wrapper(*ingridients):
      print('В ваш бутерброд добавлены: салат, ананас')
      fn(ingridients + ('Салат', 'Ананас'))
   return wrapper
@add_new
def recepy_sandwich(ingridients):
   print('Сейчас в вашем бутерброде следующие ингридиенты:')
   for i in ingridients:
      print(i)
recepy_sandwich('помидоры', 'огурцы')


