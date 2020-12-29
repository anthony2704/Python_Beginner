import random
n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("Nhap mot so duong: "))
    if guess > 0:
        if guess > to_be_guessed:
            print ("Can so nho hon")
        else:
            print ("Can so lon hon")
    else:
        print ("Ban bo cuoc ")
        break
else:
    print ("Congratulation. Doan chinh xac!!!")
