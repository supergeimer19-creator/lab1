log1 = "Олена Жабківська"
pass1 = "joker"
grades1 = [3, 6, 7, 10]
log2 = "Микита Нікольчук"
pass2 = "poor"
grades2 = [2, 3, 5, 7]
log3 = "Вадим Білінський"
pass3 = "Toosxs"
grades3 = [3, 6, 7, 10]
log4 = "Данил Нематюкаюсь"
pass4 = "Точно"
grades4 = [4, 6, 9, 10]
a = True
while a == True:
    log = input("Vvidit login: ")
    password = input("Vvedit parol: ")
    grades = []
    if log == log1 and password == pass1:
        grades = grades1
        print("Grades:", grades)

        goodgrades = 0
        badgrades = 0

        for i in grades:
            if i >= 5 and i <= 12:
                goodgrades = goodgrades + 1
            elif i >= 1 and i <= 4:
                badgrades = badgrades + 1

        print("Good (5-12):", goodgrades)
        print("Bad (1-4):", badgrades)
        a = False
    elif log == log2 and password == pass2:
        grades = grades2
        print("Grades:", grades)

        goodgrades = 0
        badgrades = 0

        for i in grades:
            if i >= 5 and i <= 12:
                goodgrades = goodgrades + 1
            elif i >= 1 and i <= 4:
                badgrades = badgrades + 1

        print("Good (5-12):", goodgrades)
        print("Bad (1-4):", badgrades)
        a = False
    elif log == log3 and password == pass3:
        grades = grades3
        print("Grades:", grades)

        goodgrades = 0
        badgrades = 0

        for i in grades:
            if i >= 5 and i <= 12:
                goodgrades = goodgrades + 1
            elif i >= 1 and i <= 4:
                badgrades = badgrades + 1

        print("Good (5-12):", goodgrades)
        print("Bad (1-4):", badgrades)
        a = False
    elif log == log4 and password == pass4:
        grades = grades4
        print("Grades:", grades)

        goodgrades = 0
        badgrades = 0

        for i in grades:
            if i >= 5 and i <= 12:
                goodgrades = goodgrades + 1
            elif i >= 1 and i <= 4:
                badgrades = badgrades + 1

        print("Good (5-12):", goodgrades)
        print("Bad (1-4):", badgrades)
        a = False
    else:
        print("Nepravilni parol abo login\n")
    continue

