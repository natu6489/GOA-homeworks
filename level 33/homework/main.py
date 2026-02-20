# .append()
# ეს მეთოდი ამატებს ახალ ელემენტს სიის ბოლოში

# .insert(index, value)
# ეს მეთოდი ამატებს ელემენტს კონკრეტულ პოზიციაზე (index-ზე)

# .pop()
# ეს მეთოდი შლის და აბრუნებს სიის ბოლო ელემენტს
# სურვილის შემთხვევაში შეგვიძლია მივუთითოთ index, რომ კონკრეტული ელემენტი წავშალოთ




numbers = [10, 20, 30, 40, 50]

# len() ფუნქცია აბრუნებს სიის ელემენტების რაოდენობას
print(len(numbers))





numbers = []

for i in range(5):
    num = int(input("შეიყვანეთ რიცხვი: "))
    numbers.append(num)

print(numbers)






colors = ["red", "green", "blue", "yellow", "purple"]

colors.pop()  # შლის ბოლო ელემენტს

print(colors)








animals = ["dog", "cat", "elephant", "lion"]

animals.insert(1, "monkey")  # მეორე პოზიციაზე ჩასმა (index 1)

print(animals)







students = []

for i in range(3):
    name = input("შეიყვანეთ სტუდენტის სახელი: ")
    students.append(name)

students.insert(0, "Teacher")  # თავში ჩასმა
students.pop()  # ბოლო ელემენტის წაშლა

print("სიის სიგრძე:", len(students))
print("საბოლოო სია:", students)











# Custom ფუნქცია არის ფუნქცია, რომელსაც პროგრამისტი თვითონ ქმნის.

# რისთვის გამოიყენება?
# - კოდის გამარტივებისთვის
# - კოდის გამეორების თავიდან ასაცილებლად
# - პროგრამის ლოგიკის დასაყოფად

# შექმნის ეტაპები:
# 1) ვწერთ სიტყვას def
# 2) ვასახელებთ ფუნქციას
# 3) ვუთითებთ პარამეტრებს ()
# 4) ვწერთ კოდს
# 5) საჭიროების შემთხვევაში ვიყენებთ return-ს

# პარამეტრი არის ცვლადი, რომელიც ფუნქციის შექმნისას იწერება
# არგუმენტი არის რეალური მნიშვნელობა, რომელსაც ფუნქციის გამოძახებისას გადავცემთ






def sum_numbers(a, b):
    return a + b

print(sum_numbers(5, 7))









def check_even(number):
    if number % 2 == 0:
        print("რიცხვი ლუწია")
    else:
        print("რიცხვი კენტია")

check_even(8)





def kvadratunia(number):
    return number * number

print(kvadratunia(6))






def to_uppercase(text):
    return text.upper()

print(to_uppercase("hello"))






def full_name(name, surname):
    print("მომხმარებლის სრული სახელი არის:", name, surname)

full_name("Natia", "Mumladze")












