masalar = dict()
for a in range(20):
    masalar[a] = 0


def hesap_ekleme():
    masa_no = int(input("Masa numarası giriniz: "))
    bakiye = masalar[masa_no]
    eklenecek_ucret = float(input("Eklenecek ücret: "))
    guncel_bakiye = bakiye + eklenecek_ucret
    masalar[masa_no] = guncel_bakiye
    print(f"Masa {masa_no} için güncel bakiye: {guncel_bakiye} TL")
    print("İşleminiz tamamlandı.")


def hesap_odeme():
    masa_no = int(input("Masa numarası giriniz: "))
    bakiye = masalar[masa_no]
    print(f"Masa {masa_no} için hesap: {bakiye} TL")
    masalar[masa_no] = 0
    print(f"Masa {masa_no} için hesap sıfırlandı. İşleminiz tamamlandı.")


def dosya_kontrolü(dosya_adi):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            veri = dosya.read().splitlines()  # Satırları al
            print("Dosyadan okunan veriler:", veri)  # Debug amaçlı, dosya içeriğini görelim
            for a in range(len(veri)):
                masalar[a] = float(veri[a])
    except FileNotFoundError:
        with open(dosya_adi, "w", encoding="utf-8") as dosya:
            print(f"{dosya_adi} dosyası bulunamadı, yeni bir dosya oluşturuldu.")


def dosya_guncelle(dosya_adi):
    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        for a in range(20):
            bakiye = str(masalar[a])
            dosya.write(bakiye + "\n")
        print(f"{dosya_adi} dosyasına güncel veriler kaydedildi.")  # Debug amaçlı


def ana_islemler():
    dosya_kontrolü("bakiye.txt")


while True:
    print("""
        Yuksel Uygun Restaurant

        1) Masaları Görüntüle
        2) Hesap Ekle
        3) Hesap Ödeme
        Q) Çıkış

        """)
    secim = input("Yapılacak İşlemi Giriniz: ")
    if secim == "1":
        for a in range(20):
            print(f"Masa {a} için hesap: {masalar[a]}")
    elif secim == "2":
        hesap_ekleme()
    elif secim == "3":
        hesap_odeme()
    elif secim.lower() == "q":
        print("Çıkış yapılıyor..")
        break
    else:
        print("Hatalı işlem yaptınız.")
    dosya_guncelle("bakiye.txt")
    input("Ana menüye dönmek için Enter'a basınız.")

ana_islemler()
