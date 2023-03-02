def rotate_clockwise(lst):
    last_element = lst[-1]
    for i in range(len(lst) - 1, 0, -1):
        lst[i] = lst[i - 1]
    lst[0] = last_element
my_list = [1, 2, 3, 4, 5]
rotate_clockwise(my_list)
print(my_list)