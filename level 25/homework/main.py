#index არის ელემენტის პოზიცია სიაში (list), სტრინგში (string) ან სხვა მიმდევრობაში. index-ი იწყება 0-დან და არა 1-დან.

# სია ელემენტებით
fruits = ["apple", "banana", "orange"]

# index-ები:
# "apple"  -> index 0
# "banana" -> index 1
# "orange" -> index 2

# ჩვეულებრივი (დადებითი) index-ები
# დაბეჭდავს პირველ ელემენტს (index 0)
print(fruits[0])   # apple

# დაბეჭდავს მეორე ელემენტს (index 1)
print(fruits[1])   # banana

# დაბეჭდავს მესამე ელემენტს (index 2)
print(fruits[2])   # orange

# უარყოფითი index-ები

#უარყოფითი index გამოიყენება მაშინ, როცა გვინდა ბოლოსკენ მივწვდეთ ელემენტებს.

# უარყოფითი index-ები:
# -1 -> ბოლო ელემენტი
# -2 -> ბოლოსწინა
# -3 -> მესამედან ბოლო

# დაბეჭდავს ბოლო ელემენტს
print(fruits[-1])  # orange

# დაბეჭდავს ბოლოსწინა ელემენტს
print(fruits[-2])  # banana