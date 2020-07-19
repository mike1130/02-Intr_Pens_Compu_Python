user_1 = input('Cual es su nombre: ')
age_1 = int(input('Cual es su edad: '))

user_2 = input('Cual es su nombre: ')
age_2 = int(input('Cual es su edad: '))

if age_1>age_2:
    print(f'{user_1} es mayor que {user_2} con un diferencia de {age_1-age_2} años')
elif age_1<age_2:
    print(f'{user_2} es mayor que {user_1} con un diferencia de {age_2-age_1} años')
else:
    print(f'{user_1} tiene la misma edad que {user_2}, siendo la edad {age_1} años')
