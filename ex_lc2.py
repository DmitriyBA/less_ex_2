target = int(input("Введите цифру, для которой хотите найти индекс в списке: "))
count = int(input("Количество элементов в списке: "))
numbers = [0 for item in range(count)]

for item in range(count):
    numbers[item] = int(input(f"Введите цифру для {item} индекса списка: "))


def index_target(numbers: list, target: int) -> int:
    """
    Функция находит индекс для элемента, если он есть в списке или возвращает
    близкий к этому индексу элемент
    """

    #число/цифра есть в списке
    for item in range(len(numbers)):
        if numbers[item] == target:
            index = item
            return index

    #число/цифра не найдена и больше всех чисел/цифр списка
    k = 0
    for item in range(len(numbers)):
        if target > numbers[item]:
            k += 1
    index = k
    return index

    #число/цифра не найдена и есть число, которое больше целевого
    k = 0
    for item in range(len(numbers)):
        if target > numbers[item]:
            k += 1
    index = k
    return index


print(index_target(numbers, target))
print(numbers)