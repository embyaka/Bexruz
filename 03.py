import turtle

# Shakl chizish funksiyalari
def kvadrat(tomon_uzunligi):
    for _ in range(4):
        t.forward(tomon_uzunligi)
        t.left(90)

def uchburchak(tomon_uzunligi):
    for _ in range(3):
        t.forward(tomon_uzunligi)
        t.left(120)

def doira(radius):
    t.circle(radius)

# Asosiy dastur
def main():
    global t
    t = turtle.Turtle()  # Turtle obyektini yaratamiz
    t.speed(1)  # Chizish tezligi

    # Foydalanuvchidan ma'lumotlarni so'raymiz
    print("Quyidagi shakllardan birini tanlang:")
    print("1 - Kvadrat")
    print("2 - Uchburchak")
    print("3 - Doira")
    tanlov = input("Tanlovingizni raqamini kiriting (1/2/3): ")

    try:
        tanlov = int(tanlov)  # Foydalanuvchi kiritgan ma'lumotni butun songa o'tkazamiz
        if tanlov not in [1, 2, 3]:
            print("Noto'g'ri tanlov! Iltimos, 1, 2 yoki 3 ni kiriting.")
            return

        # Shakl o'lchamini so'raymiz
        if tanlov == 1 or tanlov == 2:
            o_lcham = float(input("Shakl tomonining uzunligini kiriting: "))
        elif tanlov == 3:
            o_lcham = float(input("Doira radiusini kiriting: "))

        # Tanlangan shaklni chizamiz
        if tanlov == 1:
            kvadrat(o_lcham)
        elif tanlov == 2:
            uchburchak(o_lcham)
        elif tanlov == 3:
            doira(o_lcham)

        print("Shakl muvaffaqiyatli chizildi!")
    except ValueError:
        print("Xato: Noto'g'ri ma'lumot kiritildi. Iltimos, raqam kiriting.")

    turtle.done()  # Dastur tugaganda oynani yopmaslik

# Dasturni ishga tushiramiz
if __name__ == "__main__":
    main()
