def calculate_chocolates(N, C, M):
    chocolates_eaten = N // C  # Спочатку з'їдаємо всі куплені батончики
    wrappers = chocolates_eaten  # Кількість обгорток, які є після споживання батончиків

    while wrappers >= M:
        new_chocolates = wrappers // M  # Кількість батончиків, які можна отримати за обмін обгорток
        chocolates_eaten += new_chocolates
        wrappers = wrappers % M + new_chocolates

    return chocolates_eaten


# Зчитуємо кількість тестів
T = int(input())

# Обробляємо кожен тест
for _ in range(T):
    N, C, M = map(int, input().split())
    result = calculate_chocolates(N, C, M)
    print(result)
