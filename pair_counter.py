"""Дана последовательность целых чисел. Определите минимальную сумму
пар элементов массива, расстояние (разница) между индексами которых равно 2.
Если таких пар нет, выведите 0."""


def pair_counter(elements):
    list_elements = elements.split(" ")
    count_elements = len(list_elements)
    if count_elements < 3:
        return 0
    else:
        list_elements = list(map(int, list_elements))
        min_number = float("inf")
        for i in range(count_elements - 2):
            print(min_number)
            current_number = list_elements[i] + list_elements[i + 2]
            if current_number < min_number:
                min_number = current_number
        return min_number


test_1 = "3 2 1"
test_2 = "1 1 12 1 8 7 6 1 4 1 1 1"
test_3 = "4 3 2 1"
test_4 = "7 6 5 4 3 2 1"

print(pair_counter(test_2))
