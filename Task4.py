"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""
def imt(number):
    if number < 18.5:
        return 'Недостаточный вес'
    elif 18.5 <= number <= 25:
        return 'ИМТ в норме'
    elif number > 25:
        return 'Избыточный вес'

def imt_general(weight, height):
    _number = (weight / (height * height))
    print('Ваш ИМТ =', _number)
    print(imt(_number))


imt_general(int(input('Введите вес:')), int(input('Введите рост:')))