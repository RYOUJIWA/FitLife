import time

WATER_PER_KG = 30
WATER_VOLUME_IN_ML = 1000

print('ДОБРО ПОЖАЛОВАТЬ В FitLife!')
print('-' * 80)

name = input('Как я могу к вам обращаться? ')
age = int(input('Сколько вам лет? '))
weight = float(input('Какой ваш вес? '))
# Не знаю как реализовать допуск ввода с запятой
height = float(
    input('Ваш рост? (укажите согласно примеру: 1.82 м) ')
) # Нет идей для реализации защиты от дурака самостоятельно, без применения ИИ

# Рассчет ИМТ
bmi = weight / (height ** 2)
bmi = round(bmi, 1)

# Оценка ИМТ
if bmi < 18.5:
    bmi_status = "Недостаточная масса тела"
elif 18.5 < bmi < 25:
    bmi_status = "Нормальная масса тела"
elif 25 < bmi < 30:
    bmi_status = "Избыточная масса тела"
else:
    bmi_status = "Ожирение"

# Рассчет воды
water_ml = weight * WATER_PER_KG
water_l = water_ml / WATER_VOLUME_IN_ML

# Склоняем слово "Лет"
if 11 <= age % 100 <= 19:
    age_word = 'лет'
elif age % 10 == 1:
    age_word = 'год'
elif 2 <= age % 10 <= 4:
    age_word = 'года'
else:
    age_word = 'лет'

# "Анимация" для души
print('FitLife считает... Подождите...', flush=True)
time.sleep(1.5)


def app_is_calculating():
    """Выводит рассчитанные данные пользователя."""
    print(f'Имя пользователя: {name}')
    print(f'Возраст пользователя: {age} {age_word}.')
    print(f'Индекс массы тела: {bmi} - {bmi_status}')
    print(f'Норма воды в день: {water_l:.2f} литра в день')


app_is_calculating()
