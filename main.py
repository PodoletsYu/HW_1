# Задача 2: Найдите сумму цифр трехзначного числа.

# n = int (input('Введите 3х значное число: '))
# a = n % 10
# n = n // 10
# b = n % 10
# n = n // 10
# c = n
# print ('Сумма числе 3х значного числа = ', a + b + c)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# a = int (input('Введите кол-во сделанных журавликов: '))
# k = int ((a/3)*2)
# p = int ((k/2)/2)
# s = int (p)
# print (p, k, s)

#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

#вероятно задачу можно решить проще и с минимальным кол-вом строк через срезы, но я не совсем поняла как с ними работать, буду разбираться.

# n = int (input('Введите шестизначное число: '))
# if  99999 < n < 1000000:
#     t1 = n // 1000
#     t2 = n % 1000
#     a1 = t1 % 10
#     a2 = t2 % 10
#     t1 = t1 // 10
#     t2 = t2 // 10
#     b1 = t1 % 10
#     b2 = t2 % 10
#     t1 = t1 // 10
#     t2 = t2 // 10
#     c1 = t1
#     c2 = t2
#     summ1 = a1 + b1 + c1
#     summ2 = a2 + b2 + c2
#     if summ1 == summ2:
#         print("Yes")
#     else: print ("No")
# else: print ('Error, Введите 6ти значное число') 

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n,m,k = int(input('Введите 1-ю сторону: ')),int(input('Введите 2-ю сторону: ')),int(input('Введите кол-во долек: '))
if k < n*m and k % n == 0 or k % m == 0:
    print('Yes')
else: print('No')


