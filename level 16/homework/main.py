for i in range(10, -11, -1):
    print(i)




for i in range(1, 101):
    if i % 2 == 1:
        print(i)




correct_password = "goa123"
attempts = 3

while attempts > 0:
    password = input("შეიყვანეთ პაროლი: ")

    if password == correct_password:
        print("Password is correct!")
        break
    else:
        attempts -= 1
        if attempts == 0:
            print("Password is incorrect! Attempts finished.")
            break
        else:
            print("Password is incorrect! Try again")
            print("დარჩენილი მცდელობა:", attempts, "დან")









