boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']


boys_no_match =  ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls_no_match = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

case = input("Введите номер теста. 0 - есть пары, 1 - пары не совпали: ")

# Блок case и разные массивы оставил для наглядности проверок
if case == '0':
    if len(boys) == len(girls):
        for i in range(len(boys)):
            print(sorted(boys)[i] + " и " + sorted(girls)[i])

elif case == '1':
    if len(boys_no_match) != len(girls_no_match):
        print("Внимание, кто-то может остаться без пары.")
else:
    print("Введите корректный вариант")