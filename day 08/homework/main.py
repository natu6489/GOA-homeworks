# type არის ფუნქცია რომელიც ამოწმებს მისთვის გადაცემულ მონაცემის ტიპს
print(type("help"))
print(type(46))
print(type(36.37))
print(type(True))


# data conversion ნიშნავს მონაცემის ერთი ტიპიდან მეორეში გადაყვანას
print(int("456"))
print(int("2478"))
print(int("239"))
print(str(345))
print(str(int(32.32)))


a = input("enter number 1:  ")
b = input("enter number 2:  ")
c = input("enter number 3:  ")

print(a)
print(b)
print(c)

print(str(a)+str(b)+str(c))



a = (input("enter your name:  "))
b = (input("enter a number:   "))
print(a)
print(b)
print(a*(int(b)))