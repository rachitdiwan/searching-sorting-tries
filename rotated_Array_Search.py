def sort(inputlist):
    start = 0
    end = len(inputlist)-1
    while True:
        midpoint = (start + end)//2
        if inputlist[midpoint] < inputlist[end] and inputlist[midpoint]<inputlist[start]:
            if inputlist[midpoint] < inputlist[midpoint-1]:
                break
            else:
                end = midpoint
        elif inputlist[midpoint] > inputlist[start]:
            start = midpoint
    new_list = inputlist[midpoint:]+inputlist[:midpoint]
    rotend = len(inputlist[midpoint:])
    new = [new_list, rotend]
    return new

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    x = sort(input_list)
    input_list = x[0]
    rot_end = x[1]
    start = 0
    end = len(input_list)-1
    flag = False
    while start<=end:
        mid_point = (start+end)//2
        if input_list[mid_point]<number:
           start = mid_point+1
        elif input_list[mid_point]>number:
            end = mid_point
        elif input_list[mid_point] == number:
            flag = True
            break
    if flag:
        if number >= input_list[rot_end]:
            return mid_point-rot_end
        else:
            return (mid_point+rot_end)
    else:
        return -1                

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4],6])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])