total = 0

for i in range(5):
    number = int(input("Please enter the number: "))
    total += number

print("რიცხვების ჯამია:", total)

if total % 2 == 0:
    print("number is even")
else:
    print("number is odd")






while True:
    num = int(input("შეიყვანეთ რიცხვი: "))

    if num % 5 == 0 and num % 7 == 0:
        print("თქვენ შემოიყვანეთ:", num)
        break 




















balance = int(input("შეიყვანეთ თქვენი ბალანსი: "))

# ნივთები პრიორიტეტებით:
# 1) ლეპტოპი - 1500ლ
# 2) ტელეფონი - 1000ლ
# 3) ფეხსაცმელი - 100ლ
# 4) პერანგი - 50ლ
# 5) რვეული - 5ლ

if balance >= 1500:
    print("შეგიძლიათ იყიდოთ: ლეპტოპი")
elif balance >= 1000:
    print("შეგიძლიათ იყიდოთ: ტელეფონი")
elif balance >= 100:
    print("შეგიძლიათ იყიდოთ: ფეხსაცმელი")
elif balance >= 50:
    print("შეგიძლიათ იყიდოთ: პერანგი")
elif balance >= 5:
    print("შეგიძლიათ იყიდოთ: რვეული")
else:
    print("სამწუხაროდ, თქვენი ბალანსი საკმარისი არ არის არცერთი ნივთისთვის.")



















num = int(input("შეიყვანეთ რიცხვი: "))

if num > 0:
    print("რიცხვი დადებითია.")
elif num < 0:
    print("რიცხვი უარყოფითია.")
else:
    print("რიცხვი ნულია.")
    