import time #Импортировал модуль, чтобы использовать его в конце


WATER_PER_KG = 30
WATER_VOLUME = 1000 #Обозначил заранее константы
print('ДОБРО ПОЖАЛОВАТЬ В FitLife!')
print('-'*80) #Начальный экран программы

#Спрашиваем нужные вводные
name = input('Как я могу к вам обращаться? ')
age = int(input('Сколько вам лет? '))
height = float(
    input('Ваш рост? (укажите согласно примеру: 1.82 м) ')
) 
weight = float(input('Какой ваш вес? '))

#Дальше идет расчет индекса массы тела
bmi = weight / (height ** 2)
bmi = round(bmi, 1)

#Рассчет количества воды, необходимой в сутки
water_ml = weight * WATER_PER_KG
water_l = water_ml / WATER_VOLUME
water_l = round(water_l, 2)

print('FitLife считает... Подождите...', flush=True) 
time.sleep(3) #Вывод сообщения с просьбой подождать

def app_is_calculating():
    print(f'Имя пользователя: {name}')
    print(f'Возраст пользователя: {age} лет.')
    print(f'Индекс массы тела: {bmi}.')
    print(f'Норма воды в день: {water_l:.2f} л./день')
    return

app_is_calculating() #И выводим весь полученный результат одной функцией
