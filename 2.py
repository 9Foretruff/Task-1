def fib(k):
    fibonacci = []
    a, b = 0, 1
    for i in range(k):
        fibonacci.append(a)
        a, b = b, a + b
    return fibonacci


k = int(input("Введите количество чисел Фибоначчи для вывода: "))

fibonacci_numbers = fib(k)
print(f"Первые {k} чисел Фибоначчи: {fibonacci_numbers}")
