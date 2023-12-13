#220501003/Yavuz Selim Gürsoy/Bilgisayar Müh.
#220502015/Talha Tuna/Yazılım Müh.

class CargoBay:
    def __init__(self, bayName):
        self.bayName = bayName
        self.capacity = 750
        self.ton20 = 0
        self.ton30 = 0
        self.shipLoad = 0
        self.truckControl = None

        self.countryDict = {"Mordor": [0, 0, 0],
                            "Oceania": [0, 0, 0],
                            "Lilliputa": [0, 0, 0],
                            "Neverland": [0, 0, 0]}

        # Ülkelerin adının karşılığında oraya giden toplam, 20 ve 30 tonluk yüklerin sayısı bulunuyor.
        # Birinci index toplam yükü, ikincisi 20 tonluk yük sayısını, üçüncüsü ise 30 tonluk yük sayısını belirtiyor.


        # Initializer fonksiyonu istif alanı nesnesinin ismini, kapasitesini,
        # 20 tonluk yük sayısını, 30 tonluk yük sayısını, gemiye yüklenecek yük miktarını
        # ( bu sınıfın unload() üye fonksiyonu içerisinde kullanmak için ),
        # kontrol değişkenini ( Tırın doluluk oranını kontrol etmek için ) tutar.

    def isFull(self):
        return self.capacity < 20

        # İstif alanı nesnesinin kapasitesi 20'nin altına düştüğünde True, düşmediğinde False döndürür.

    def isEmpty(self):
        return self.capacity == 750

        # İstif alanı nesnesinin kapasitesi 750 olduğunda True, olmadığında False döndürür.

    def load(self, truck):
        if self.capacity == 750:
            print(f"\x1b[38;5;46mİstif alanı {self.bayName}, şu an boş.")
            # İstif alanı boş olduğunda bir mesaj yazdır.

        if self.capacity - truck.truckLoad < 0 or self.capacity == 0:
            print(f"\x1b[38;5;1mİstif alanı {self.bayName}, {truck.licensePlate} tırındaki yükü alamaz. Tır sıraya ekleniyor.")

            self.truckControl = False
            # Eğer istif alanındaki yük, tırın üzerindeki yükü alamayacak durumdaysa;
            # bunu bir mesaj ile belirt ve kontrol değişkenini False' a çevir.

        else:
            self.truckControl = True

            self.capacity -= truck.truckLoad
            self.ton20 += truck.ton20
            self.ton30 += truck.ton30
            # Kapasite dolu değilse kapasiteyi yük kadar azalt, tırın 20 ve 30 tonu kadar artır.
            # (Hiçbir zaman sorunlu çalışmayacak çünkü tırın zaten ya 20 ya da 30 ton taşıyor olması lazım, ikisini birden taşıyamaz.)

            destinationInfo = self.countryDict[truck.destination]

            destinationInfo[0] += truck.truckLoad
            destinationInfo[1] += truck.ton20
            destinationInfo[2] += truck.ton30

            # Ülkelere göre ayır, Örneğin Neverland'e gidecek bir yükleri 20, 30 ve toplam yük şeklinde işaretle.

            print(f"\x1b[38;5;208m{truck.licensePlate} tırı, istif alanı {self.bayName}'e {truck.destination}'a gitmesi için {truck.truckLoad} ton yük bıraktı. Kalan istif kapasitesi: {self.capacity}")

        return self.truckControl

    def unload(self, ship):
        loads = self.countryDict[ship.destination]
        # Ülke sözlüğünün içinden geminin gideceği ülkeye giden toplam yük 20, 30 tonluk yük sayısını loads listesine yerleştirir.

        if loads[0] == 0:
            pass
            # Boşsa hiç döngüye girmez.

        if ship.capacity - 30 >= 0 and loads[2] > 0 and self.shipLoad < ship.min:
            self.shipLoad += 30
            loads[0] -= 30
            loads[2] -= 1
            self.capacity += 30
            ship.capacity -= 30
            self.ton30 -= 1

            # 30 tonluk yük sayısı 0 dan fazlaysa ve gemi 30 tonluk yük alabilecek durumdaysa ve
            # gemiye toplam yüklenen yük geminin minimum kapasitesinden küçükse; toplam yükü 30 azalt, gemi yükünü 30 artır,
            # istif alanı kapasitesini 30 artır, gemi kapasitesini 30 azalt, 30 tonluk yük sayısını 1 azalt.

            print(f"\x1b[38;5;226mİstif alanı {self.bayName}'den {30} ton {ship.name} gemisine aktarıldı. '{ship.name}' kapasitesi: {ship.capacity}, Kalan istif kapasitesi {self.capacity}")

            if self.shipLoad >= ship.min:
                self.shipLoad = 0
                return False

                # Eğer gemi yükü geminin minimum kapasitesinden büyük ya da eşitse geminin bir daha yüklenmemesi için
                # False döndür ve gemi yükü değişkenini 0'a eşitle.

            else:
                self.shipLoad = 0
                return True

        if ship.capacity - 20 >= 0 and loads[1] > 0 and self.shipLoad < ship.min:
            self.shipLoad += 20
            loads[0] -= 20
            loads[1] -= 1
            self.capacity += 20
            ship.capacity -= 20
            self.ton20 -= 1

            # 20 tonluk yük sayısı 0 dan fazlaysa ve gemi 20 tonluk yük alabilecek durumdaysa ve
            # gemiye toplam yüklenen yük geminin minimum kapasitesinden küçükse; toplam yükü 20 azalt, gemi yükünü 20 artır,
            # istif alanı kapasitesini 20 artır, gemi kapasitesini 20 azalt, 20 tonluk yük sayısını 1 azalt.

            print(f"\x1b[38;5;226mİstif alanı {self.bayName}'den {20} ton {ship.name} gemisine aktarıldı. '{ship.name}' kapasitesi: {ship.capacity}, Kalan istif kapasitesi: {self.capacity}")

            if self.shipLoad >= ship.min:
                self.shipLoad = 0
                return False

                # Eğer gemi yükü geminin minimum kapasitesinden büyük ya da eşitse geminin bir daha yüklenmemesi için
                # False döndür ve gemi yükü değişkenini 0'a eşitle.


            else:
                self.shipLoad = 0
                return True

        else:
            return False

    def printInfo(self):
        for i in self.countryDict:
            totalLoad = self.countryDict.get(i)[0]
            load20 = self.countryDict.get(i)[1]
            load30 = self.countryDict.get(i)[2]
            print(f"\x1b[38;5;90m{i}' a giden toplam yük: {totalLoad}\n20 tonluk yük sayısı: {load20}\n30 tonluk yük sayısı: {load30}\n")

            # printInfo fonksiyonu istif alanının özelliklerini ekrana bastırmaya yarar.
            # printInfo fonksiyonları çıktı verilirken kullanılmadı. Sadece kod yazarken ilerlememizi izlemek için kullanıldı.

class Truck:
    def __init__(self, arriveTime, licensePlate, destination, ton20, ton30, truckLoad, cost):
        self.arriveTime = int(arriveTime)
        self.licensePlate = licensePlate
        self.destination = destination
        self.truckLoad = int(truckLoad)
        self.cost = int(cost)
        self.ton20 = int(ton20)
        self.ton30 = int(ton30)


        # Initializer fonksiyonu tır nesnesinin geliş zamanını, plakasını, varış noktasını, 20 tonluk yük miktarını,
        # 30 tonluk yük miktarını, toplam yük miktarını ve tırın istif alanına ulaşma maaliyetini tutar.

    def printInfo(self):
        print(f"\x1b[38;5;255mPlaka: {self.licensePlate}\n"
              f"t zamanı: {self.arriveTime}\n"
              f"Varış noktası: {self.destination}\n"
              f"Yük: {self.truckLoad}\n"
              f"Maaliyet: {self.cost}\n"
              f"20 tonluk yük: {self.ton20}\n"
              f"30 tonluk yük: {self.ton30}\n")

        # printInfo fonksiyonu bir üst yorum satırındaki tır özelliklerini ekrana bastırmaya yarar.

class Ship:
    def __init__(self, arriveTime, name, capacity, destination):
        self.arriveTime = int(arriveTime)
        self.name = name
        self.capacity = int(capacity)
        self.destination = destination
        self.min = capacity * 95 / 100
        self.constcap = capacity

        # Initializer fonksiyonu gemi nesnesinin geliş zamanını, ismini, kapasitesini, varış noktasını,
        # alabileceği minimum yükü ( % 95 ) ve kalıcı kapasiteyi ( main fonksiyonunda kullanmak için ) tutar.

    def isFull(self):
        return self.capacity == 0 or self.constcap - self.capacity >= self.min

        # Gemi nesnesinin tamamı ya da % 95' i dolduğunda True, dolmadığında False döndürür.

    def printInfo(self):
        print(f"\x1b[38;5;255mİsim: {self.name}\n"
              f"t zamanı: {self.arriveTime}\n"
              f"Varış noktası: {self.destination}\n"
              f"Yük kapasitesi: {self.capacity}\n")

        # printInfo fonksiyonu bir üst yorum satırındaki gemi özelliklerini ekrana bastırmaya yarar ( kalıcı kapasite hariç ).

def group(aList):
    aDict = dict()

    for innerList in aList:
        ndx0 = innerList[0]

        if ndx0 in aDict:
            aDict[ndx0].append(innerList)
        else:
            aDict[ndx0] = [innerList]

    returnList = list(aDict.values())

    return returnList
    # group() fonksiyonu kendisine parametre olarak gelen bir listedeki
    # iç listelerin birinci elemanları aynı olanları başka bir iç listeye alır.

def order(eventDir, shipDir, grouped=False):
    shipFile = open(shipDir, "r", encoding="windows-1254")
    eventFile = open(eventDir, "r", encoding="windows-1254")

    eventCsv = eventFile.readlines()
    shipCsv = shipFile.readlines()

    eventCsv.pop(0), shipCsv.pop(0)

    eventUnordList = list()
    shipUnordList = list()


    for j in eventCsv:
        j = j.rstrip("\n").split(",")
        eventUnordList.append(j)

    eventOrdList = sorted(eventUnordList, key=lambda x: (int(x[0]), int((x[1][9:]).rstrip("'"))))

    if grouped == True:
        eventOrdList = group(eventOrdList)

    for i in shipCsv:
        i = i.rstrip("\n").split(",")
        shipUnordList.append(i)

    shipOrdList = sorted(shipUnordList, key=lambda x: (int(x[0]), int(x[1])))

    return eventOrdList, shipOrdList
    # order() fonksiyonu parametre olarak aldığı iki dizin string'ini
    # ( olaylar ve gemiler dizinleri ) iki listeye atar ve bu listeleri önce 0. indise sonra 1. indise göre sıralar.

def simulation():
    files = order("olaylar.csv", "gemiler.csv", grouped=True)

    events = files[0]
    ships = files[1]

    cargoBay1 = CargoBay("1")
    cargoBay2 = CargoBay("2")

    truckList = list()
    shipList = list()
    ship = None


    for currentTime in range(1, int(events[-1][-1][0]) + 1):
        # Tır listesinin son satırındaki tırın ulaşma saatine kadar döngüyü sürdür.
        craneLimit = 20

        while currentTime == int(events[0][0][0]):
            for i in events[0]:
                truckList.append(i)
            events.pop(0)
            break
            # Eğer tır nesnesinin ulaşma zamanı şu anki zamana eşitse, bu nesneyi tır kuyruğuna ekle.

        if len(ships) != 0:
            while currentTime == int(ships[0][0]):
                shipList.append(ships[0])
                ships.pop(0)
                break
                # Eğer gemi nesnesinin ulaşma zamanı şu anki zamana eşitse, bu nesneyi gemi kuyruğuna ekle.

        print(f"\x1b[38;5;14mt = {currentTime}")

        while len(truckList) != 0 and craneLimit > 0:
            if cargoBay1.isFull() and cargoBay2.isFull():
                print("\x1b[38;5;1mİstif alanları dolu.")
                break
                # Eğer iki istif alanı da doluysa, bunu belirt.

            else:
                truckAttributes = truckList.pop(0)
                truck = Truck(int(truckAttributes[0]), truckAttributes[1], truckAttributes[2],
                                int(truckAttributes[3]), int(truckAttributes[4]),
                                int(truckAttributes[5]), int(truckAttributes[6]))
                 # Eğer istif alanlarında yer varsa, tır listesinden bir tır özelliği listesi çekip bunu bir tır nesnesine çevir.

            if cargoBay1.isFull() and not cargoBay2.isFull():
                control = cargoBay2.load(truck)
                craneLimit -= 1

                if control is False:
                    truckList.insert(0, truckAttributes)
                    break


            elif not cargoBay1.isFull() and cargoBay2.isFull():
                control = cargoBay1.load(truck)
                craneLimit -= 1

                if control is False:
                    truckList.insert(0, truckAttributes)
                    break


            elif not cargoBay1.isFull() and not cargoBay2.isFull():
                control = cargoBay1.load(truck)
                craneLimit -= 1

                if control is False:
                    truckList.insert(0, truckAttributes)
                    break
            # Üç durumdan (Birinci istif alanı dolu ikincisi boşsa, birincisi boş ikincisi doluysa, her ikisi de boşsa) birini seç ve tır nesnesini belirtilen istif alanına boşalt. Eğer ki istif alanı bu yükü alacak durumda değilse, tır nesnesinin özelliklerini tırlar listesinin en başına yeniden yerleştir ve döngüyü kır.


        if len(shipList) != 0:

            if ship is None:
                shipAttrs = shipList[0]
                ship = Ship(int(shipAttrs[0]), shipAttrs[1], int(shipAttrs[2]), shipAttrs[3])
                # Gemi listesi doluysa ve gemi nesnesi yoksa bir gemi nesnesi oluştur.

            while ship is not None and craneLimit > 0:

                while (cargoBay1.countryDict[ship.destination])[0] != 0 and ship.isFull() is False and craneLimit > 0:
                    if cargoBay1.unload(ship) == False:
                        break

                    craneLimit -= 1

                    if craneLimit == 0:
                        break

                    if cargoBay1.unload(ship) is True:
                        if craneLimit == 0:
                            break
                        else:
                            craneLimit -= 1
                     # Eğer birinci istif alanında gemiyle aynı yere gidecek bir yük varsa, gemi dolu değilse ve gemi yükü alabilecek durumdaysa gemiyi yükle ve vinç sınırını azalt. Gemi yükü alamayacak durumdaysa döngüyü kır.


                while (cargoBay2.countryDict[ship.destination])[0] != 0 and ship.isFull() is False and craneLimit > 0:
                    if cargoBay2.unload(ship) == False:
                        break

                    craneLimit -= 1

                    if craneLimit == 0:
                        break

                    if cargoBay2.unload(ship) is True:
                        if craneLimit == 0:
                            break
                        else:
                            craneLimit -= 1
                    # Eğer ikinci istif alanında gemiyle aynı yere gidecek bir yük varsa, gemi dolu değilse ve gemi yükü alabilecek durumdaysa gemiyi yükle ve vinç sınırını azalt. Gemi yükü alamayacak durumdaysa döngüyü kır.


                if ship.isFull() is True:
                    shipList.pop(0)
                    print(f"\x1b[38;5;90m{ship.name} tamamen yüklendi.")
                    ship = None
                    break
                    # Gemi tamamen yüklendiyse gemi nesnesini sil, gemiyi bekleyenler listesinden kaldır ve bunu kullanıcıya bildir.

                if cargoBay1.isEmpty() and cargoBay2.isEmpty():
                    print("\x1b[38;5;46mİstif alanları boş.")
                    break
                    # Eğer istif alanları boşsa (hiçbir gemi yük alamayacağından) kullanıcıya bildir.

                else:
                    break

        if craneLimit == 0:
            print("\x1b[38;5;196mVinç ısındı!")
            # Eğer vinç saatte 20 den fazla işlem yapmaya çalışırsa kullanıcıya bildir ve döngüyü kır.

def main():
    control = True

    files = order("olaylar.csv", "gemiler.csv")
    trucks = files[0]
    ships = files[1]

    truckDict = {}
    shipDict = {}

    for truck in trucks:
        truckDict.update({(truck[0], truck[1]): (truck[2], truck[3], truck[4], truck[5], truck[6])})

    for ship in ships:
        shipDict.update({ship[1]: (ship[0], ship[2], ship[3])})



    print(f"\x1b[38;5;14mLiman Otomasyonu\n"
          f"-------------------------------------\n"
          f"\x1b[38;5;200m0) Simülasyonu oynat\n"
          f"1) Tır bilgilerine eriş\n"
          f"2) Gemi bilgilerine eriş\n"
          f"3) Çıkış\n")

    while control == True:

        try:
            choice = int(input("\x1b[38;5;147m\nSeçeneğinizi girin (rakamlarla): "))

            if choice == 0:
                print("\x1b[38;5;34mSimülasyon başlatılıyor...")
                simulation()

            if choice == 1:
                aTime = input("\x1b[38;5;147mTırın istif alanına ulaşma saatini girin: ")
                lPlate = input("Tırın plakasını girin: ")

                print(f"\n\x1b[38;5;208mPlaka: {lPlate}\n"
                      f"İstif alanına ulaştığı saat: {aTime}\n"
                      f"Varış noktası: {truckDict[(aTime, lPlate)][0]}\n"
                      f"20 tonluk yük miktarı: {truckDict[(aTime, lPlate)][1]}\n"
                      f"30 tonluk yük miktarı: {truckDict[(aTime, lPlate)][2]}\n"
                      f"Toplam yük miktarı: {truckDict[(aTime, lPlate)][3]}\n"
                      f"Maaliyet: {truckDict[(aTime, lPlate)][4]}\n")


            if choice == 2:
                name = input("\x1b[38;5;147mGeminin ismini girin: ")

                print(f"\n\x1b[38;5;220mİsim: {name}\n"
                      f"İstif alanına ulaştığı saat: {shipDict[name][0]}\n"
                      f"Varış noktası: {shipDict[name][2]}\n"
                      f"Kapasitesi: {shipDict[name][1]}\n")

            if choice == 3:
                break


            else:
                print("\n\x1b[38;5;196mMenüde olmayan bir değer girildi. Program sonlandırılıyor")
                break

        except KeyError:
            print("\n\x1b[38;5;196mGirdiğiniz veriler, herhangi bir tır veya gemiyle eşleşmiyor.")

        except ValueError:
            print("\n\x1b[38;5;196mYanlış girdi(ler) girildi. Lütfen belirtilen şekilde girdinizi girin.")

main()