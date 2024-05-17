def find_common_element(list1,list2):
    common_element =[]
    for item in list1:
        if item in list2:
            common_element.append(item)
            
    return common_element
list_a =[4,5,3,6,2]
list_b = [1,2,3,4,5]
common = find_common_element(list_a,list_b)
print(common)