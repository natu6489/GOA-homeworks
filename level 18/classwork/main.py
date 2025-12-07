num = int(input("შეიყვანე რიცხვი: "))

if num > 50:
    print(num * 5)
else:
    print(num ** 2)



password = input("შეიყვანე პაროლი: ")

if password == "goa123":
    print("Password is correct!")
else:
    print("Incorrect password!")



num = int(input("შეიყვანე რიცხვი: "))

total = 0

for i in range(1, num + 1):
    total += i