def ascending_order(numbers_list):
    #Termination condidition for recursive function
    if len(numbers_list) <= 1:
        return
    #mid point of my list - dividing my list into 2 parts
    mid = len(numbers_list)//2
    #left part of the list
    left_list = numbers_list[:mid]
    #right part of the list 
    right_list = numbers_list[mid:]
    #sorting the lists both right and left parts of the list
    ascending_order(left_list)
    ascending_order(right_list)
    #lengths of the individual lists
    len_left_list = len(left_list)
    len_right_list = len(right_list)
    
    i = j = k = 0
    #Coppying the list data to temporary list using loop
    while i < len_left_list and j < len_right_list:
        if left_list[i] < right_list[j]:
            numbers_list[k] = left_list[i]
            i+=1
        else:
            numbers_list[k] = right_list[j]
            j+=1
        k+=1
    # Checking for any left out elements
    while i < len_left_list:
        numbers_list[k] = left_list[i]
        i+=1
        k+=1

    while j < len_right_list:
        numbers_list[k] = right_list[j]
        j+=1
        k+=1
    return numbers_list
def descending_order(numbers_list):
    if len(numbers_list) <= 1:
        return

    mid = len(numbers_list)//2

    left_list = numbers_list[:mid]
    right_list = numbers_list[mid:]

    descending_order(left_list)
    descending_order(right_list)
    len_left_list = len(left_list)
    len_right_list = len(right_list)

    i = j = k = 0

    while i < len_left_list and j < len_right_list:
        if right_list[j] > left_list[i]:
            numbers_list[k] = right_list[j]
            j+=1
        else:
            numbers_list[k] = left_list[i]
            i+=1
        k+=1

    while i < len_left_list:
        numbers_list[k] = left_list[i]
        i+=1
        k+=1

    while j < len_right_list:
        numbers_list[k] = right_list[j]
        j+=1
        k+=1
    return numbers_list
def take_inputs():
    #taking number of inputs
    n = int(input())
    numbers_list = []
    #taking n inputs
    for i in range(n):
        numbers = int(input())
        numbers_list.append(numbers)
    #taking sorting order as an input
    sort_order = input()
    lower_case_sort_order = sort_order.lower()
    if(lower_case_sort_order == "asc"):
        result = ascending_order(numbers_list)
    elif(lower_case_sort_order == "desc"):
        result = descending_order(numbers_list)
    else : 
        print("Not a valid Sorting Order")
    print(result)

take_inputs()
print("I hope you are satisfied with the result.To repeat it again, Y or N? N")
input_yes_or_no = input().lower()
if(input_yes_or_no == "y"):
    take_inputs()
else:
    print("Thank You")