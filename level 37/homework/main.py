#Default პარამეტრი არის ფუნქციის პარამეტრი, რომელსაც თავიდანვე აქვს მინიჭებული მნიშვნელობა.
#ანუ თუ ფუნქციის გამოძახების დროს არგუმენტს არ გადავცემთ, მაშინ გამოიყენება ის მნიშვნელობა, რაც default-ად აქვს გაწერილი.


def greet(name="Natia"):
    print("Hello", name)






def print_letters(name="Natia"):
    for letter in name:
        print(letter)

