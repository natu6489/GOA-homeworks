for i in range(1, 6):
    print(i)

i = 1

while i <= 5:
    print(i)
    i += 1


num = 0

if num > 0:
    print("დადებითი")
elif num < 0:
    print("უარყოფითი")
else:
    print("ნული")



for i in range(1, 11):
    if i % 2 == 0:
        print(i, "ლუწია")
    else:
        print(i, "კენტია")





num = 1

while num <= 15:
    if num % 3 == 0:
        print(num)
    num += 1





numbers = [-2, 0, 5, 10]

for n in numbers:
    if n > 0:
        print(n, "დადებითია")
    elif n < 0:
        print(n, "უარყოფითია")
    else:
        print(n, "ნულია")





age = int(input("შეიყვანეთ ასაკი: "))

if age >= 0:
    if age < 18:
        print("არასრულწლოვანი")
    else:
        print("სრულწლოვანი")
else:
    print("არასწორი ასაკი")







