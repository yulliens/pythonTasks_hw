def answer_machine(message):
    message = message.lower()
    if 'расп' in message:
        print('Пн 18.00-19.30, Ср 18.00-19.30, Сб 11.00-12.30')
    elif 'трен' in message:
        print('+79624105334')
    elif 'плат' in message:
        print('Сумма к оплате:2500 рублей')
    elif 'скидк' in message:
        print('3 занятия по цене 1')
    elif 'адрес' in message:
        print('ул. Транспортная, 6')
    else:
        print('Не можем понять ваш запрос, повторите еще раз')