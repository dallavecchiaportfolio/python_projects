number = 134

answer = int(input("Enter your guessing: "))

if answer > number:
    print("Maior")
elif answer < number:
    print("Menor")
else:
    print("Acertou")