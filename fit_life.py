import time

WATER_PER_KG = 30
WATER_VOLUME = 1000

print('ДОБРО ПОЖАЛОВАТЬ В FitLife!')
print('-' * 80)

name = input('Как я могу к вам обращаться? ')
age = int(input('Сколько вам лет? '))
weight = float(input('Какой ваш вес? '))
height = float(
    input('Ваш рост? (укажите согласно примеру: 1.82 м) ')
)

bmi = weight / (height ** 2)
bmi = round(bmi, 1)

water_ml = weight * WATER_PER_KG
water_l = water_ml / WATER_VOLUME
water_l = round(water_l, 2)

print('FitLife считает... Подождите...', flush=True)
time.sleep(1.5)


def app_is_calculating():
    """Выводит рассчитанные данные пользователя."""
    print(f'Имя пользователя: {name}')
    print(f'Возраст пользователя: {age} лет.')
    print(f'Индекс массы тела: {bmi}.')
    print(f'Норма воды в день: {water_l:.2f} л./день')
    return


app_is_calculating()
