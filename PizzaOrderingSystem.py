import csv
from datetime import datetime

# Pizza sınıfı ve alt sınıflarının oluşturulması
class Pizza():
    def __init__(self):
        self.description = ""
        self.cost = 0.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class ClassicPizza(Pizza):
    def __init__(self):
        self.description = "Klasik Pizza"
        self.cost = 75.0


class MargheritaPizza(Pizza):
    def __init__(self):
        self.description = "Margarita Pizza"
        self.cost = 70.0


class TurkishPizza(Pizza):
    def __init__(self):
        self.description = "Türk Pizza"
        self.cost = 85.5


class DominosPizza(Pizza):
    def __init__(self):
        self.description = "Dominos Pizza"
        self.cost = 92.5


class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class Olive(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Zeytin"
        self.cost = 3.0


class Mushroom(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mantar"
        self.cost = 3.5


class GoatCheese(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Keçi Peyniri"
        self.cost = 4.5


class Meat(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Et"
        self.cost = 7.5


class Onion(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Sogan"
        self.cost = 4


class Corn(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Misir"
        self.cost = 2.5

# open_menu() metodu ile menu.txt adında bir dosya oluşturularak dosya içeriği ekrana yazdırılır. Olası dosya hataları için try-except blokları kullanılmıştır.
def open_menu():
    try:
        file = open("menu.txt", "w")
        menu = "* Lütfen Bir Pizza Tabani Seçiniz:\n1: Klasik\n2: Margarita\n3: TürkPizza\n4: Sade Pizza\n* ve sececeginiz sos:\n11: Zeytin\n12: Mantarlar\n13: Keçi Peyniri\n14: Et\n15: Soğan\n16: Misir\n* Tesekkür ederiz!"
        file.write(menu)
        file = open("menu.txt", "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("Hata!")
    finally:
        file.close()

# main() metodu ile open_menu() metodu çağrılır, kullanıcıdan alınan girdiler tarih bilgileriyle beraber Orders_Database.csv isimli dosyaya yazılır.
def main():
    open_menu()
    # while döngüleri ve try-except blokları ile kullanıcıdan doğru girdi alınması ve olası hataların önlenmesi amaçlanmıştır.
    while True:
        while True:
            try:
                pizza_choice = int(input("Pizza tabani seciminiz: "))
                break
            except ValueError:
                print("Lütfen 1 ile 4 arasi bir deger giriniz.\n")
        if pizza_choice == 1:
            pizza = ClassicPizza()
            break
        elif pizza_choice == 2:
            pizza = MargheritaPizza()
            break
        elif pizza_choice == 3:
            pizza = TurkishPizza()
            break
        elif pizza_choice == 4:
            pizza = DominosPizza()
            break
        else:
            print("Lütfen 1 ile 4 arasi bir secim yapiniz.\n")

    while True:
        while True:
            try:
                sauce_choice = int(input("Sos seciminiz: "))
                break
            except ValueError:
                print("Lütfen 11 ile 16 arasi bir deger giriniz.\n")
        if sauce_choice == 11:
            sauce = Olive(pizza)
            break
        elif sauce_choice == 12:
            sauce = Mushroom(pizza)
            break
        elif sauce_choice == 13:
            sauce = GoatCheese(pizza)
            break
        elif sauce_choice == 14:
            sauce = Meat(pizza)
            break
        elif sauce_choice == 15:
            sauce = Onion(pizza)
            break
        elif sauce_choice == 16:
            sauce = Corn(pizza)
            break
        else:
            print("Lütfen 11 ile 16 arasi bir secim yapiniz.\n")
    print("--------------------------")
    print(sauce.get_description())
    print("Tutar:",sauce.get_cost(), "₺")
    print("--------------------------")
    while True:
        # Buradaki try bloğunda kullanıcının girdiği isim, baş harfleri büyük,diğer harfleri küçük olacak şekilde düzeltilmektedir.
        try:
            name = str(input("Adınız: "))
            name = name.lower()
            name = name.capitalize()
            break
        except ValueError:
            print("Hatalı giriş! Lütfen tekrar deneyiniz.")
    while True:
        try:
            tc = int(input("TC no: "))
            tc = str(tc)
            if len(tc) < 11 or len(tc) > 11:
                print("TC no 11 hane olmalıdır. Lütfen tekrar deneyiniz.")
                continue
            break
        except ValueError:
            print("Hatalı giriş! Lütfen tekrar deneyiniz.")
    while True:
        try:
            credit_card = int(input("Kart no: "))
            credit_card = str(credit_card)
            if len(credit_card) < 16 or len(tc) > 16:
                print("Kart no 16 hane olmalı.")
                continue
            break
        except ValueError:
            print("Hatalı giriş! Lütfen tekrar deneyiniz.")
    while True:
        try:
            password = int(input("Sifre: "))
            password = str(password)
            if len(password) < 4 or len(password) > 4:
                print("Gecersiz sifre! Lütfen tekrar deneyiniz.")
                continue
            break
        except ValueError:
            print("Hatalı giriş! Lütfen tekrar deneyiniz.")
    # Sipariş tarihi
    now = datetime.now()
    date = datetime.strftime(now,'%c')
    # Sipariş bilgileri veritabanına kaydedilir.
    data = [name,tc,credit_card,sauce.get_description(),sauce.get_cost(),date,password]
    with open('Orders_Database.csv','a') as file_db:
        writer = csv.writer(file_db)
        writer.writerow(data)
    # Sipariş tamamlandıktan sonra detaylar ekrana yazdırılır.
    print("--------------------------")
    print("SİPARİŞ TAMAMLANDI\n")
    print(f"Ad: {name}\nTarih: {date} \nSipariş: {sauce.get_description()}\nTutar: {sauce.get_cost()}")
    print("--------------------------")
main()
