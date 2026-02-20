# .upper()
# ეს ფუნქცია მთელ ტექსტს აქცევს დიდ (uppercase) ასოებად

text1 = "hello"
print(text1.upper())   # HELLO

text2 = "Python"
print(text2.upper())   # PYTHON

text3 = "good morning"
print(text3.upper())   # GOOD MORNING



# .lower()
# ეს ფუნქცია მთელ ტექსტს აქცევს პატარა (lowercase) ასოებად

text4 = "HELLO"
print(text4.lower())   # hello

text5 = "PYTHON"
print(text5.lower())   # python

text6 = "Good Night"
print(text6.lower())   # good night



# .capitalize()
# ეს ფუნქცია მხოლოდ პირველი ასოს აქცევს დიდად,
# დანარჩენ ასოებს კი პატარა ასოებად

text7 = "hello"
print(text7.capitalize())   # Hello

text8 = "pYtHoN"
print(text8.capitalize())   # Python

text9 = "good morning"
print(text9.capitalize())   # Good morning



# .title()
# ეს ფუნქცია თითოეული სიტყვის პირველ ასოს აქცევს დიდად

text10 = "hello world"
print(text10.title())   # Hello World

text11 = "good morning teacher"
print(text11.title())   # Good Morning Teacher

text12 = "python programming language"
print(text12.title())   # Python Programming Language



# .find()
# ეს ფუნქცია ეძებს კონკრეტულ სიმბოლოს ან სიტყვას
# და აბრუნებს მის index-ს (ადგილმდებარეობას)
# თუ ვერ იპოვა, აბრუნებს -1-ს

text13 = "hello world"
print(text13.find("w"))   # 6

text14 = "python programming"
print(text14.find("pro"))   # 7

text15 = "good night"
print(text15.find("z"))   # -1


# Dot notation არის მეთოდი,
# რომლის საშუალებითაც ობიექტზე ვიძახებთ მის ფუნქციას ან თვისებას.

# მაგალითად:
text = "hello"

# აქ text არის string ობიექტი
# .upper() არის მისი ფუნქცია (method)
print(text.upper())

# ანუ წერტილის (.) საშუალებით ვიძახებთ
# კონკრეტული ტიპის ფუნქციებს.

# dot notation გამოიყენება:
# - string ფუნქციების გამოსაძახებლად
# - list ფუნქციების გამოსაძახებლად
