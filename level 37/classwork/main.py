def my_len(text):
    count = 0
    for i in text:
        count += 1
    return count

print(my_len("hello"))



def my_find(text, letter):
    index = 0
    
    for i in text:
        if i == letter:
            return index
        index += 1
    
    return -1

print(my_find("hello", "l"))






def my_insert(lst, index, value):
    new_list = []
    i = 0
    
    for item in lst:
        if i == index:
            new_list.append(value)
        new_list.append(item)
        i += 1
    
    return new_list

numbers = [1, 2, 3]
print(my_insert(numbers, 1, 99))




