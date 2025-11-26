save_password = 7777
balance = 5600
summa = 0

menu = ["Balance" , "Sms xabarnoma ", "Tolovlar" , "Parolni ozgartirish ", "Naqt pul olish"]

kirish = int(input("Salom! Parolingizni kiriting : "))

if kirish == save_password:
    print("Xush kelibsiz , menudan birini tanlang !")
    print(f"1-{menu[0]}")
    print(f"2-{menu[1]}")
    print(f"3-{menu[2]}")
    print(f"4-{menu[3]}")
    print(f"5-{menu[4]}")
else:
    print("Parol notogri")
    exit()

menu_tanlov = int(input("Menudan birini tanlang : "))

if menu_tanlov == 1:
    print(f"Sizning xisobingizda : {balance} so'm bor")

elif menu_tanlov == 2:
    print("Sms xabarnomani yoqish")
    print("Sms xabarnomani ochirish")

elif menu_tanlov == 3:

    while True:
        print("Tolovlar bolimi")
        print("1- Elektr")
        print("2- Gaz")
        print("3- Suv")
        print("4- Jarimalar")
        print("5- Mobil aloqa uchun tolov")
        print("0- Orqaga qaytish")

        tolov_tanlov = int(input("Tolovni tanlang: "))

        if tolov_tanlov == 0:
            print(f"Menuga qaytingiz {menu_tanlov}")

        elif tolov_tanlov == 1:
            hisob = int(input("Elektr hisobingizni kiriting: "))
            yangi_miq = int(input("Miqdorni kiriting: "))
            if yangi_miq <= balance:
                balance -= yangi_miq
                print("Tolov otkazildi")
            else:
                print("Balans yetarli emas")

        elif tolov_tanlov == 2:
            hisob = int(input("Gaz hisobingizni kiriting: "))
            yangi_miq = int(input("Miqdorni kiriting: "))
            if yangi_miq <= balance:
                balance -= yangi_miq
                print("Tolov otkazildi")
            else:
                print("Balans yetarli emas")

        elif tolov_tanlov == 3:
            hisob = int(input("Suv hisobingizni kiriting: "))
            yangi_miq = int(input("Miqdorni kiriting: "))
            if yangi_miq <= balance:
                balance -= yangi_miq
                print("Tolov otkazildi")
            else:
                print("Balans yetarli emas")

        elif tolov_tanlov == 4:
            hisob = int(input("Jarima raqamini kiriting: "))
            yangi_miq = int(input("Miqdorni kiriting: "))
            if yangi_miq <= balance:
                balance -= yangi_miq
                print("Tolov otkazildi")
            else:
                print("Balans yetarli emas")

        elif tolov_tanlov == 5:
            hisob = input("Telefon raqamingizni kiriting: ")
            yangi_miq = int(input("Miqdorni kiriting: "))
            if yangi_miq <= balance:
                balance -= yangi_miq
                print("Tolov otkazildi")
            else:
                print("Balans yetarli emas")

elif menu_tanlov == 4:
    print("Parolni ozgartirish")

elif menu_tanlov == 5:
    summa = float(input("Summani kiriting: "))
    if summa <= balance:
        balance -= summa
        print(f"Siz {summa} so'm yechib oldingiz")
        print(f"Balansingizda {balance} so'm qoldi")
    else:
        print("Hisobingizda yetarli mablag yoq")
        print(f"Hisobingiz {balance}")
