Задание: ввести число и найти сумму его цифр.
n = int(input()) Вводим число.
a = n // 100 Находим первую цифру.
b = n // 10 % 10 Находим вторую цифру.
c = n % 10 Находим третью цифру.
print(a + b + c) Складываем их друг с другом и выводим ответ.
