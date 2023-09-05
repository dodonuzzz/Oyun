class Oyuncu:
    def __init__(self, ad, takim, guc, envanter):
        self.ad = ad
        self.takim = takim
        self.guc = guc
        self.envanter = envanter

    def __str__(self):
        return f"{self.ad}, {self.takim},{self.guc}, {self.envanter}"


class Nesne:
    def __init__(self, ad, deger, aciklama, tur):
        self.ad = ad
        self.deger = deger
        self.aciklama = aciklama
        self.tur = tur

    def __str__(self):
        return f"{self.ad}, {self.deger}, {self.aciklama}, {self.tur}"


class UlasimYolu:
    def __init__(self, ad, hedef_mekanlar):
        self.ad = ad
        self.hedef_mekanlar = hedef_mekanlar

    def __str__(self):
        return f"{self.ad}, {self.hedef_mekanlar}"


class Mekan:
    def __init__(self, ad, nesneler, aciklama, yol):  # esyalar ve silahlar olarak listeleri almalısınız
        self.ad = ad
        self.nesneler = nesneler
        self.aciklama = aciklama
        self.yol = yol

    def __str__(self):
        return f"{self.ad}, {self.nesneler}, {self.aciklama}, {self.yol}"


marmaray_uskudar = UlasimYolu("Marmaray", ["Kadıköy", "Eminönü"])
otobus_uskudar = UlasimYolu("Otobüs", ["Beykoz", "Ataşehir"])
metro_uskudar = UlasimYolu("Metro", ["Ümraniye"])
vapur_uskudar = UlasimYolu("Vapur", ["Beşiktaş"])
marmaray_kadikoy = UlasimYolu("Marmaray", ["Bostancı", "Göztepe", "Üsküdar"])
otobus_kadikoy = UlasimYolu("Otobüs", ["Ataşehir", "Beykoz"])
metro_kadikoy = UlasimYolu("Metro", ["Sabiha Gökçen Havalimanı"])
vapur_kadikoy = UlasimYolu("Vapur", ["Beşiktaş", "Eminönü"])
otobus_beykoz = UlasimYolu("Otobüs", ["Üsküdar", "Ümraniye", "Kadıköy"])
vapur_beykoz = UlasimYolu("Vapur", ["Sarıyer"])
otobus_besiktas = UlasimYolu("Otobüs", ["Sarıyer"])
metro_besiktas = UlasimYolu("Metro", ["Şişli"])
vapur_besiktas = UlasimYolu("Vapur", ["Kadıköy", "Üsküdar"])
marmaray_eminonu = UlasimYolu("Marmaray", ["Bakırköy", "Üsküdar"])
tram1_eminonu = UlasimYolu("Tramvay", ["Bağcılar"])
tram2_eminonu = UlasimYolu("Tramvay", ["Eyüpsultan"])
vapur_eminonu = UlasimYolu("Vapur", ["Kadıköy"])
metro1_umraniye = UlasimYolu("Metro", ["Üsküdar", "Dudullu", "Sancaktepe"])
metro2_umraniye = UlasimYolu("Metro", ["Ataşehir", "Göztepe"])
otobus_umraniye = UlasimYolu("Otobüs", ["Beykoz"])
otobus_atasehir = UlasimYolu("Otobüs", ["Üsküdar", "Kadıköy", "Sancaktepe"])
metro1_atasehir = UlasimYolu("Metro", ["Bostancı", "Dudullu"])
metro2_atasehir = UlasimYolu("Metro", ["Ümraniye", "Göztepe"])


def oyun():
    global Nesne
    pistol = Nesne("Pistol", 10, "Bildiğin tabanca işte.", "Silah")
    molotof_kokteyli = Nesne("Molotof Kokteyli", 50, "Aşk gibi silah... Adamı yakar kül eder.", "Silah")
    av_tufegi = Nesne("Av Tüfeği", 40, "Güçlü bir tüfek.", "Silah")
    doner_bicagi = Nesne("Döner Bıçağı", 5, "Döner Bıçağı", "Silah")
    uzi = Nesne("Uzi", 45, "Adamı delik deşik eder.", "Silah")
    lav_silahi = Nesne("Lav Silahı", 45, "3 saniye bakınca Esra'nın şelalesi gibi yanıyosun.", "Silah")
    iskender_kebap = Nesne("İskender Kebap", 10, "Ağzının tadını biliyosun.", "Eşya")
    bira = Nesne("Bira", 10, "Aç buz gibi Efes", "Eşya")
    kondom = Nesne("Kondom", 30, "OOO Reis beline kuvvet.", "Eşya")
    altin = Nesne("Altın", 100, "Zenginsin knk", "Eşya")
    ilac = Nesne("İlaç", 50, "Güçlü bir ilaç", "Eşya")
    takim_elbise = Nesne("Takım Elbise", 25, "Ateş ediyossunnnnnn.", "Eşya")

    ulasim_yollari = {
        'Üsküdar': {'Marmaray': marmaray_uskudar, 'Otobüs': otobus_uskudar, 'Metro': metro_uskudar,
                    'Vapur': vapur_uskudar},
        'Kadıköy': {'Marmaray': marmaray_kadikoy, 'Otobüs': otobus_kadikoy, 'Metro': metro_kadikoy,
                    'Vapur': vapur_kadikoy},
        'Eminönü': {'Marmaray': marmaray_eminonu, 'Tramvay1': tram1_eminonu, 'Tramvay2': tram2_eminonu,
                    'Vapur': vapur_eminonu},
        'Ümraniye': {'Metro1': metro1_umraniye, 'Metro2': metro2_umraniye, 'Otobüs': otobus_umraniye},
        'Beykoz': {'Otobüs': otobus_beykoz, 'Vapur': vapur_beykoz},
        'Beşiktaş': {'Otobüs': otobus_besiktas, 'Vapur': vapur_besiktas, 'Metro': metro_besiktas},
        'Ataşehir': {'Otobüs': otobus_atasehir, 'Metro1': metro1_atasehir, 'Metro2': metro2_atasehir},

    }

    uskudar = Mekan("Üsküdar", [iskender_kebap, doner_bicagi],
                    "Anadolu Yakası'nda Deniz Kenarında merkezi bir semt",
                    ulasim_yollari['Üsküdar'])
    kadikoy = Mekan("Kadıköy", [kondom, pistol],
                    "Boğa Heykeli, Fener Stadı, Rıhtım, Moda ve Barlar Sokağı ile Kadıköy",
                    ulasim_yollari['Kadıköy'])
    beykoz = Mekan("Beykoz", [av_tufegi],
                   "Biraz Deniz biraz Orman ancak Ormandan ayılar inebilir dostum dikkat et.",
                   ulasim_yollari['Beykoz'])
    besiktas = Mekan("Beşiktaş", [bira, molotof_kokteyli], "Üsküdar'ın karşısı. Hatunları güzeldir.",
                     ulasim_yollari['Beşiktaş'])
    eminonu = Mekan("Eminönü", [altin], "Sokaklar dar ve karışıktır.",
                    ulasim_yollari['Eminönü'])
    umraniye = Mekan("Ümraniye", [ilac, uzi], "Uzun caddeler ve yüksek binalar",
                     ulasim_yollari['Ümraniye'])
    atasehir = Mekan("Ataşehir", [takim_elbise, lav_silahi], "Gökdelenler ve iş merkezleri", ulasim_yollari['Ataşehir'])

    # Mekanları mekanlar sözlüğüne ekleyin
    mekanlar = {'Üsküdar': uskudar, 'Kadıköy': kadikoy, 'Beykoz': beykoz, 'Beşiktaş': besiktas, 'Eminönü': eminonu,
                'Ümraniye': umraniye, 'Ataşehir': atasehir}
    nesneler = {'İskender Kebap': iskender_kebap, 'Bira': bira, 'Kondom': kondom, 'Altın': altin, 'İlaç': ilac,
                'Takım Elbise': takim_elbise, 'Pistol': pistol, 'Molotof Kokteyli': molotof_kokteyli,
                'Av Tüfeği': av_tufegi, 'Döner Bıçağı': doner_bicagi, 'Uzi': uzi, 'Lav Silahı': lav_silahi}

    oyuncu = Oyuncu("Oyuncu Adı", "Takım Adı", 100, [])  # Gerekli parametreleri vermeniz gerekiyor
    mevcut_mekan = 'Üsküdar'

    def OyuncuEnvanterGoruntule(oyuncu):
        print("Envanteriniz:")
        for nesne in oyuncu.envanter:
            print(f"{nesne.ad}: {nesne.aciklama}")

    if __name__ == "__main__":
        oyuncu = Oyuncu("Oyuncu Adı", "Takım Adı", 100, [])
        mevcut_mekan = 'Üsküdar'

    while True:
        mevcut_mekan_obj = mekanlar[mevcut_mekan]  # Mekan nesnesini alın
        print(f"{mevcut_mekan}'dasınız. {mevcut_mekan_obj.aciklama}")
        if mevcut_mekan_obj.nesneler:
            print("Gördükleriniz")
            for nesne in mevcut_mekan_obj.nesneler:
                print(f"{nesne.ad}: {nesne.aciklama}")

        eylem = input("> ").strip().lower()  # Girdinin başındaki ve sonundaki boşlukları kaldırın, küçük harfe çevirin

        if mevcut_mekan == 'Üsküdar':

            secilen_hedef = input("Hangi hedefi seçiyorsunuz? ").strip()

            if secilen_hedef in marmaray_uskudar.hedef_mekanlar:
                mevcut_mekan = secilen_hedef
                print(f" Gelecek İstasyon {mevcut_mekan}. Next station {mevcut_mekan}. ")
            elif secilen_hedef in otobus_uskudar.hedef_mekanlar:
                mevcut_mekan = secilen_hedef
                print(f" Bir sonraki durak {mevcut_mekan}. ")
            elif secilen_hedef in metro_uskudar.hedef_mekanlar:
                mevcut_mekan = secilen_hedef
                print(f"Gelecek İstasyon {mevcut_mekan}. Next station {mevcut_mekan}. ")
            elif secilen_hedef in vapur_uskudar.hedef_mekanlar:
                mevcut_mekan = secilen_hedef
                print(f"Vapurumuz {mevcut_mekan} iskelesine yanaşmıştır. ")
            else:
                print("Geçerli bir hedef seçmelisiniz.")
        # ...
        elif mevcut_mekan == 'Kadıköy':

            secilen_hedef = input("Hangi hedefi seçiyorsunuz? ").strip()

            if secilen_hedef in marmaray_kadikoy.hedef_mekanlar and secilen_hedef != 'Kadıköy':
                mevcut_mekan = secilen_hedef
                print(f" Gelecek İstasyon {mevcut_mekan}. Next station {mevcut_mekan}.")

            elif secilen_hedef in otobus_kadikoy.hedef_mekanlar and secilen_hedef != 'Kadıköy':
                mevcut_mekan = secilen_hedef
                print(f" Bir sonraki durak {mevcut_mekan}.")

            elif secilen_hedef in metro_kadikoy.hedef_mekanlar and secilen_hedef != 'Kadıköy':
                mevcut_mekan = secilen_hedef
                print(f" Gelecek İstasyon {mevcut_mekan}. Next station {mevcut_mekan}.")

            elif secilen_hedef in vapur_kadikoy.hedef_mekanlar and secilen_hedef != 'Kadıköy':
                mevcut_mekan = secilen_hedef
                print(f" Vapurumuz {mevcut_mekan} iskelesine yanaşmıştır.")
            else:
                print("Geçerli bir hedef seçmelisiniz.")

        elif mevcut_mekan == 'Eminönü':

            secilen_hedef = input("Hangi hedefi seçiyorsunuz? ").strip()

            if secilen_hedef in marmaray_eminonu.hedef_mekanlar and secilen_hedef != 'Eminönü':
                mevcut_mekan = secilen_hedef
                print(f" Gelecek İstasyon {mevcut_mekan}. Next station {mevcut_mekan}.")

            elif secilen_hedef in tram1_eminonu.hedef_mekanlar and secilen_hedef != 'Eminönü':
                mevcut_mekan = secilen_hedef
                print(f" Gelecek İstasyon {mevcut_mekan}. Next station {mevcut_mekan}.")

            elif secilen_hedef in tram2_eminonu.hedef_mekanlar and secilen_hedef != 'Eminönü':
                mevcut_mekan = secilen_hedef
                print(f" Gelecek İstasyon {mevcut_mekan}. Next station {mevcut_mekan}.")

            elif secilen_hedef in vapur_eminonu.hedef_mekanlar and secilen_hedef != 'Eminönü':
                mevcut_mekan = secilen_hedef
                print(f" Vapurumuz {mevcut_mekan} iskelesine yanaşmıştır.")
            else:
                print("Geçerli bir hedef seçmelisiniz.")

        elif mevcut_mekan == 'Beykoz':

            secilen_hedef = input("Hangi hedefi seçiyorsunuz? ").strip()

            if secilen_hedef in otobus_beykoz.hedef_mekanlar and secilen_hedef != 'Beykoz':
                mevcut_mekan = secilen_hedef
                print(f" Bir sonraki durak {mevcut_mekan}.")

            elif secilen_hedef in vapur_beykoz.hedef_mekanlar and secilen_hedef != 'Beykoz':
                mevcut_mekan = secilen_hedef
                print(f"Vapurumuz {mevcut_mekan} iskelesine yanaşmıştır. ")

            else:
                print("Geçerli bir hedef seçmelisiniz.")


        elif mevcut_mekan == 'Beşiktaş':

            secilen_hedef = input("Hangi hedefi seçiyorsunuz? ").strip()

            if secilen_hedef in otobus_besiktas.hedef_mekanlar and secilen_hedef != 'Beşiktaş':
                mevcut_mekan = secilen_hedef
                print(f" Bir sonraki durak {mevcut_mekan}.")

            elif secilen_hedef in vapur_besiktas.hedef_mekanlar and secilen_hedef != 'Beşiktaş':
                mevcut_mekan = secilen_hedef
                print(f"Vapurumuz {mevcut_mekan} iskelesine yanaşmıştır. ")

            elif secilen_hedef in metro_besiktas.hedef_mekanlar and secilen_hedef != 'Beşiktaş':
                mevcut_mekan = secilen_hedef
                print(f"Gelecek İstasyon {mevcut_mekan}. Next station {mevcut_mekan}.")

            else:
                print("Geçerli bir hedef seçmelisiniz.")


        elif mevcut_mekan == 'Ümraniye':

            secilen_hedef = input("Hangi hedefi seçiyorsunuz? ").strip()

            if secilen_hedef in metro1_umraniye.hedef_mekanlar and secilen_hedef != 'Ümraniye':
                mevcut_mekan = secilen_hedef
                print(f"Gelecek İstasyon {mevcut_mekan}. Next station {mevcut_mekan}.")

            elif secilen_hedef in metro2_umraniye.hedef_mekanlar and secilen_hedef != 'Ümraniye':
                mevcut_mekan = secilen_hedef
                print(f"Gelecek İstasyon {mevcut_mekan}. Next station {mevcut_mekan}.")

            elif secilen_hedef in otobus_umraniye.hedef_mekanlar and secilen_hedef != 'Ümraniye':
                mevcut_mekan = secilen_hedef
                print(f"Bir sonraki durak {mevcut_mekan}.")

            else:
                print("Geçerli bir hedef seçmelisiniz.")


        elif mevcut_mekan == 'Ataşehir':

            secilen_hedef = input("Hangi hedefi seçiyorsunuz? ").strip()

            if secilen_hedef in otobus_atasehir.hedef_mekanlar and secilen_hedef != 'Ataşehir':
                mevcut_mekan = secilen_hedef
                print(f"Bir sonraki durak {mevcut_mekan}.")

            elif secilen_hedef in metro1_atasehir.hedef_mekanlar and secilen_hedef != 'Ataşehir':
                mevcut_mekan = secilen_hedef
                print(f"Gelecek İstasyon {mevcut_mekan}. Next station {mevcut_mekan}.")

            elif secilen_hedef in metro2_atasehir.hedef_mekanlar and secilen_hedef != 'Ataşehir':
                mevcut_mekan = secilen_hedef
                print(f"Gelecek İstasyon {mevcut_mekan}. Next station {mevcut_mekan}.")

            else:
                print("Geçerli bir hedef seçmelisiniz.")

        if eylem == "envanter":
            OyuncuEnvanterGoruntule(oyuncu)


        elif eylem.startswith("al "):
            girdi_nesneler = eylem[3:].split(',')
            alinan_nesneler = []

            for girdi_nesne in girdi_nesneler:
                girdi_nesne = girdi_nesne.strip()
                bulunan_nesne = None

                for nesne_ad, nesne in nesneler.items():
                    if nesne_ad.lower() == girdi_nesne.lower():  # Büyük/küçük harf farkını dikkate almayın
                        bulunan_nesne = nesne
                        break

                if bulunan_nesne:
                    alinan_nesneler.append(bulunan_nesne)
                else:
                    print(f"{girdi_nesne} adında bir nesne mevcut değil.")

            oyuncu.envanter.extend(alinan_nesneler)

            for alinan_nesne in alinan_nesneler:
                print(f"{alinan_nesne.ad} envanterinize eklendi.")


if __name__ == "__main__":
    oyun()
