while True:
    raw_input = input("Введите элементы массива через пробел: ")
    try:
        A = list(map(int, raw_input.strip().split()))
    except ValueError:
        print("Ошибка: введите только целые числа.")
        continue

    if len(A) < 3:
        print("Ошибка: в массиве должно быть как минимум три элемента.")
        continue

    break

max_index = A.index(max(A))
min_index = A.index(min(A))

start = min(max_index, min_index) + 1
end = max(max_index, min_index)

sum_neg = sum(x for x in A[start:end] if x < 0)

print("Сумма отрицательных элементов между максимальным и минимальным элементами в массиве:", sum_neg)
