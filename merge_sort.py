def merge(left, right):
    lefty = 0
    righty = 0
    merged = []
    while lefty < len(left) and righty < len(right):
        if left[lefty] > right[righty]:
            merged.append(right[righty])
            righty += 1
        else:
            merged.append(left[lefty])
            lefty += 1

    for val in left[lefty:]:
        merged.append(val)
    for val in right[righty:]:
        merged.append(val)
    return merged


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    midpoint = len(arr)//2
    left = arr[midpoint:]
    right = arr[:midpoint]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def rearrange_digits(input_list):
    
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    input_list = merge_sort(input_list)
    i = len(input_list)-1
    j = len(input_list)-2
    no1 = ""
    no2 = ""
    while i >= 0:
        no1 += str(input_list[i])
        i -= 2
    while j >= 0:
        no2 += str(input_list[j])
        j -= 2
    
    return [int(no1), int(no2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[3, 4, 1, 9, 6, 7], [963, 741]])
