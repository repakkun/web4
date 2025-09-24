number_str = input("Введите номер билета - 6 значений: ")

first_half_sum = int(number_str[0]) + int(number_str[1]) + int(number_str[2])
second_half_sum = int(number_str[3]) + int(number_str[4]) + int(number_str[5])

if first_half_sum == second_half_sum:
    print("Счастливый билет")
else:
    print("Несчастливый билет")