def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    next_pos_0 = 0
    next_pos_2 = len(input_list) - 1
    cursor = 0

    while cursor <= next_pos_2:
        if input_list[cursor] == 0:
            input_list[cursor] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1
            cursor += 1
        elif input_list[cursor] == 2:           
            input_list[cursor] = input_list[next_pos_2] 
            input_list[next_pos_2] = 2
            next_pos_2 -= 1
        else:
            cursor += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])