'''Given a sequence of integers. Determine the minimum sum of pairs
of array elements whose indices have a difference of 2.
If there are no such pairs, print 0.'''

'''Дана последовательность целых чисел. Определите минимальную сумму
пар элементов массива, расстояние (разница) между индексами которых равно 2.
Если таких пар нет, выведите 0.'''


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


numbers = "1 1 12 1 8 7 6 1 4 1 1 1"

print(pair_counter(numbers))
