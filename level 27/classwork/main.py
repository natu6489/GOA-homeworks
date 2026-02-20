cars = ["BMW", "Audi", "Mercedes", "Toyota", "Honda", "Ford", "Kia", "Hyundai", "Mazda", "Nissan"]
print(cars[5])



names = ["Nika", "Ana", "Luka", "Mari", "Saba", "Gio", "Nino", "Dato", "Elene", "Irakli"]


new_list = names[1:6]
print(new_list)


print(new_list[-1])



print(names[::2])


print(names[3:9:3])


first_five = names[:5]
first_five.reverse()
print(first_five)


copy_names = names[:]


names[8] = "Sophia"


print(names)
print(copy_names)




#          0  1  2    3   4
numbers = [3, 7, 12, 25, 40]


for num in numbers:
    print(num)
