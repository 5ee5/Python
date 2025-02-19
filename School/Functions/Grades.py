grades = [4, 6, 8, 5, 9, 5, 8, 7, 10, 9, 8]

def list_sum(list_to_sum: list):
    sum = 0
    for list_element in list_to_sum:
        sum += list_element

    return sum

def list_lenght(list_with_numbers: list):
    return len(list_with_numbers)

print(list_sum(grades))