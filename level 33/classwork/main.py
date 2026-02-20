names = ["Natia", "Giorgi", "Ana", "Luka", "Nino"]

new_name = input("Enter a name: ")
names.append(new_name)

names.insert(3, "Tarieli")

names.pop(4)

names.remove("Ana")

search_name = input("Enter name to search: ")

if search_name in names:
    print("Index:", names.index(search_name))
else:
    print("not index in list")










    