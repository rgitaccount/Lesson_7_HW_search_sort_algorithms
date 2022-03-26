list_1 = [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161,
           168, 175, 182, 189, 196, 203, 210, 217, 224, 231, 238, 245, 252, 259, 266, 273, 280, 287, 294, 301, 308,
           315, 322, 329, 336, 343, 350, 357, 364, 371, 378, 385, 392, 399, 406, 413, 420, 427, 434, 441, 448, 455,
           462, 469, 476, 483, 490, 497, 504, 511, 518, 525, 532, 539, 546, 553, 560, 567, 574, 581, 588, 595, 602,
           609, 616, 623, 630, 637, 644, 651, 658, 665, 672, 679, 686, 693]

list_2 = [79, 60, 45, 12, 26, 66, 7, 84, 38, 16, 86, 13, 67, 4, 17, 79, 2, 25, 12, 20, 21, 97, 4, 16, 60, 46, 93, 84,
          49, 55, 92, 31, 65, 63, 87, 72, 29, 92, 66, 58, 32, 84, 47, 11, 42, 78, 65, 1, 30, 84, 20, 29, 76, 42, 96,
          30, 6, 93, 53, 65, 39, 4, 0, 74, 94, 47, 8, 9, 100, 21, 7, 33, 43, 89, 44, 64, 17, 16, 95, 13, 19, 20, 14,
          71, 8, 38, 26, 63, 34, 82, 35, 77, 10, 57, 89, 100, 78, 31, 69, 55]


# binary search
def binary_search(value, my_list):
    N = len(my_list)
    result_ok = False
    first = 0
    last = N - 1
    while first < last:
        middle = (first + last) // 2
        if value == my_list[middle]:
            first = middle
            last = first
            result_ok = True
            pos = middle
        else:
            if value > my_list[middle]:
                first = middle + 1
            else:
                last = middle - 1

    if result_ok:
        print(f"Element is found at {pos}")
    else:
        print('Element is not found')


binary_search(77, list_1)
binary_search(76, list_1)


# Bubble sort
def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list

print(bubble_sort(list_2))













