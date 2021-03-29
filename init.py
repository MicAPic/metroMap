class Station:
    registry = []

    def __init__(self, name, line, coordinates=None, transfer=False):
        self.registry.append(self)
        self.name = name
        self.line = line
        self.id = len(self.registry) - 1
        self.coordinates = coordinates
        self.transfer = transfer

    def __str__(self):
        return f'Это станция "{self.name}" {self.line} линии (ID: {self.id})'


class Span:
    registry = []

    def __init__(self, stationA, stationB, time):
        self.registry.append(self)
        self.stations = [stationA, stationB]
        self.time = time

    def __str__(self):
        return f'Перегон м/у "{self.stations[0].name}" и "{self.stations[1].name}" составляет {self.time} мин'


PVeteranov = Station('Проспект Ветеранов', 'red', [132, 642])
LeninskyP = Station('Ленинский проспект', 'red', [134, 616])
Avtovo = Station('Автово', 'red', [139, 592])
KirovskyZ = Station('Кировский завод', 'red', [154, 560])
Narvskaya = Station('Нарвская', 'red', [181, 522])
Baltiyskaya = Station('Балтийская', 'red', [212, 494.2])
TInstitut1 = Station('Технологический институт-1', 'red', [252, 462.2], True)
Pushkinskaya = Station('Пушкинская', 'red', [313.45, 402.2], True)
Vladimirskaya = Station('Владимирская', 'red', [338, 351.2], True)
Vosstaniya = Station('Площадь Восстания', 'red', [348, 303.2], True)
Chernyshevskaya = Station('Чернышевская', 'red', [348, 265.2])
PLenina = Station('Площадь Ленина', 'red', [348, 234.2])
Vyborgskaya = Station('Выборгская', 'red', [348, 206.2])
Lesnaya = Station('Лесная', 'red', [348, 179.2])
PMuzhestva = Station('Площадь Мужества', 'red', [348, 153.2])
Politeh = Station('Политехническая', 'red', [348, 127.2])
Akademicheskaya = Station('Академическая', 'red', [348, 101])
GrazdanskiyP = Station('Гражданский проспект', 'red', [348, 74])
Murino = Station('Девяткино', 'red', [348, 49])

Kupchino = Station('Купчино', 'blue', [252, 672.2])
Zvezdnaya = Station('Звездная', 'blue', [252, 644.2])
Moskovskaya = Station('Московская', 'blue', [252, 614.2])
ParkP = Station('Парк Победы', 'blue', [252, 585.2])
Elektrosila = Station('Электросила', 'blue', [252, 558.2])
MVorota = Station('Московские ворота', 'blue', [252, 531.2])
Frunzenskaya = Station('Фрунзенская', 'blue', [252, 498.2])
TInstitut2 = Station('Технологический институт-2', 'blue', [252, 462.2], True)
Sennaya = Station('Сенная площадь', 'blue', [252, 351.2], True)
Nevskiy = Station('Невский проспект', 'blue', [252, 303.2], True)
Gorkovskaya = Station('Горьковская', 'blue', [252, 231.2])
PSkaya = Station('Петроградская', 'blue', [252, 196.2])
ChRechka = Station('Чёрная речка', 'blue', [252, 158.2])
Pionerskaya = Station('Пионерская', 'blue', [252, 133.2])
Udelnaya = Station('Удельная', 'blue', [252, 107.2])
Ozerki = Station('Озерки', 'blue', [252, 82.2])
PProsvet = Station('Проспект Просвещения', 'blue', [252, 57.2])
Parnas = Station('Парнас', 'blue', [252, 33.2])

Rybatskoe = Station('Рыбацкое', 'green', [451, 657.2])
Obuhovo = Station('Обухово', 'green', [451, 624.2])
Proletarskaya = Station('Пролетарская', 'green', [451, 590.2])
Lomonosovskaya = Station('Ломоносовская', 'green', [451, 547.2])
Elizarovskaya = Station('Елизаровская', 'green', [451, 507.2])
PNevskogo1 = Station('Площадь Александра Невского-1', 'green', [450, 351.2], True)
Mayakovskaya = Station('Маяковская', 'green', [348, 303.2], True)
GDvor = Station('Гостиный двор', 'green', [252, 303.2], True)
VOskaya = Station('Василеостровская', 'green', [129, 293])
Primorskaya = Station('Приморская', 'green', [72, 258])
Novokrestovskaya = Station('Зенит', 'green')
Begovaya = Station('Беговая', 'green', [48, 143])

Spasskaya = Station('Спасская', 'DarkOrange2', [252, 351.2], True)
Dostoevskaya = Station('Достоевская', 'DarkOrange2', [338, 351.2], True)
LigovskyP = Station('Лиговский проспект', 'DarkOrange2', [406, 351.2])
PNevskogo2 = Station('Площадь Александра Невского-2', 'DarkOrange2', [450, 351.2], True)
Novocherkasskaya = Station('Новочеркасская', 'DarkOrange2', [495, 362.2])
Ladozhskaya = Station('Ладожская', 'DarkOrange2', [509, 401.2])
PBolshevikov = Station('Проспект Большевиков', 'DarkOrange2', [509, 445.2])
Dybenko = Station('Улица Дыбенко', 'DarkOrange2', [509, 486.2])

Shushary = Station('Шушары', 'purple', [362, 668.2])
Dunaiskaya = Station('Дунайская', 'purple', [362, 641.2])
PSlavy = Station('Проспект Славы', 'purple', [362, 614.2])
Mezhdunarodnaya = Station('Муждународная', 'purple', [362, 586.2])
Buharestskaya = Station('Бухарестская', 'purple', [362, 559.2])
Volkovskaya = Station('Волковская', 'purple', [362, 524.2])
OKanal = Station('Обводный канал', 'purple', [347.45, 450.2])
Zvenigorodskaya = Station('Звенигородская', 'purple', [313.45, 402.2], True)
Sadovaya = Station('Садовая', 'purple', [252, 351.2], True)
Admiralteiskaya = Station('Адмиралтейская', 'purple', [209.45, 328.2])
Sportivnaya = Station('Спортивная', 'purple', [154.45, 241.2])
Sportivnaya2 = Station('Спортивная (В.О.)', 'purple', [132.45, 265.2])
Chkalovskaya = Station('Чкаловская', 'purple', [152.45, 212.2])
KrestovskyO = Station('Крестовский остров', 'purple', [152.45, 183.2])
StarayaD = Station('Старая Деревня', 'purple', [152.45, 142.5])
KomendantskiyP = Station('Комендантский проспект', 'purple', [152.45, 113.5])

for station in Station.registry:
    print(station)

PVeteranovLeninskyP = Span(PVeteranov, LeninskyP, 2)
LeninskyPAvtovo = Span(LeninskyP, Avtovo, 3)
AvtovoKirovskyZ = Span(Avtovo, KirovskyZ, 2)
KirovskyZNarvskaya = Span(KirovskyZ, Narvskaya, 4)
NarvskayaBaltiyskaya = Span(Narvskaya, Baltiyskaya, 3)
BaltiyskayaTInstitut1 = Span(Baltiyskaya, TInstitut1, 2)
TInstitut1Pushkinskaya = Span(TInstitut1, Pushkinskaya, 2)
PushkinskayaVladimirskaya = Span(Pushkinskaya, Vladimirskaya, 2)
VladimirskayaVosstaniya = Span(Vladimirskaya, Vosstaniya, 2)
VosstaniyaChernyshevskaya = Span(Vosstaniya, Chernyshevskaya, 3)
ChernyshevskayaPLenina = Span(Chernyshevskaya, PLenina, 3)
PLeninaVyborgskaya = Span(PLenina, Vyborgskaya, 3)
VyborgskayaLesnaya = Span(Vyborgskaya, Lesnaya, 3)
LesnayaPMuzhestva = Span(Lesnaya, PMuzhestva, 3)
PMuzhestvaPoliteh = Span(PMuzhestva, Politeh, 2)
PolitehAkademicheskaya = Span(Politeh, Akademicheskaya, 2)
AkademicheskayaGrazhdanskiyP = Span(Akademicheskaya, GrazdanskiyP, 4)
GrazdanskiyPMurino = Span(GrazdanskiyP, Murino, 4)

KupchinoZvezdnaya = Span(Kupchino, Zvezdnaya, 3)
ZvezdnayaMoskovskaya = Span(Zvezdnaya, Moskovskaya, 5)
MoskovskayaParkP = Span(Moskovskaya, ParkP, 3)
ParkPElektrosila = Span(ParkP, Elektrosila, 2)
ElektrosilaMVorota = Span(Elektrosila, MVorota, 2)
MVorotaFrunzenskaya = Span(MVorota, Frunzenskaya, 3)
FrunzenskayaTInstitut2 = Span(Frunzenskaya, TInstitut2, 2)
TInstitut2Sennaya = Span(TInstitut2, Sennaya, 2)
SennayaNevskiy = Span(Sennaya, Nevskiy, 2)
NevskiyGorkovskaya = Span(Nevskiy, Gorkovskaya, 4)
GorkovskayaPSkaya = Span(Gorkovskaya, PSkaya, 2)
PSkayaChRechka = Span(PSkaya, ChRechka, 4)
ChRechkaPionerskaya = Span(ChRechka, Pionerskaya, 3)
PionerskayaUdelnaya = Span(Pionerskaya, Udelnaya, 3)
UdelnayaOzerki = Span(Udelnaya, Ozerki, 3)
OzerkiPProsvet = Span(Ozerki, PProsvet, 2)
PProsvetParnas = Span(PProsvet, Parnas, 3)

RybatskoeObuhovo = Span(Rybatskoe, Obuhovo, 4)
ObuhovoProletarskaya = Span(Obuhovo, Proletarskaya, 3)
ProletarskayaLomonosovskaya = Span(Proletarskaya, Lomonosovskaya, 4)
LomonosovskayaElizarovskaya = Span(Lomonosovskaya, Elizarovskaya, 3)
ElizarovskayaPNevskogo1 = Span(Elizarovskaya, PNevskogo1, 4)
PNevskogo1Mayakovskaya = Span(PNevskogo1, Mayakovskaya, 3)
MayakovskayaGDvor = Span(Mayakovskaya, GDvor, 3)
GDvorVOskaya = Span(GDvor, VOskaya, 4)
VOskayaPrimorskaya = Span(VOskaya, Primorskaya, 4)
PrimorskayaNovokrestovskaya = Span(Primorskaya, Novokrestovskaya, 4)
NovokrestovskayaBegovaya = Span(Novokrestovskaya, Begovaya, 4)

SpasskayaDostoevskaya = Span(Spasskaya, Dostoevskaya, 4)
DostoevskayaLigovskyP = Span(Dostoevskaya, LigovskyP, 2)
LigovskyPPNevskogo2 = Span(LigovskyP, PNevskogo2, 2)
PNevskogo2Novocherkasskaya = Span(PNevskogo2, Novocherkasskaya, 3)
NovocherkasskayaLadozhskaya = Span(Novocherkasskaya, Ladozhskaya, 3)
LadozhskayaPBolshevikov = Span(Ladozhskaya, PBolshevikov, 3)
PBolshevikovDybenko = Span(PBolshevikov, Dybenko, 3)

ShusharyDunaiskaya = Span(Shushary, Dunaiskaya, 3)
DunaiskayaPSlavy = Span(Dunaiskaya, PSlavy, 3)
PSlavyMezhdunarodnaya = Span(PSlavy, Mezhdunarodnaya, 2)
MezhdunarodnayaBuharestskaya = Span(Mezhdunarodnaya, Buharestskaya, 3)
BuharestskayaVolkovskaya = Span(Buharestskaya, Volkovskaya, 3)
VolkovskayaOKanal = Span(Volkovskaya, OKanal, 3)
OKanalZvenigorodskaya = Span(OKanal, Zvenigorodskaya, 3)
ZvenigorodskayaSadovaya = Span(Zvenigorodskaya, Sadovaya, 3)
SadovayaAdmiralteiskaya = Span(Sadovaya, Admiralteiskaya, 2)
AdmiralteiskayaSportivnaya = Span(Admiralteiskaya, Sportivnaya, 3)
SportivnayaChkalovskaya = Span(Sportivnaya, Chkalovskaya, 2)
ChkalovskayaKrestovskyO = Span(Chkalovskaya, KrestovskyO, 3)
KrestovskyOStarayaD = Span(KrestovskyO, StarayaD, 3)
StarayaDKomendantskiyP = Span(StarayaD, KomendantskiyP, 4)

SennayaSpasskaya = Span(Sennaya, Spasskaya, 4)
SpasskayaSadovaya = Span(Spasskaya, Sadovaya, 3)
SadovayaSennaya = Span(Sadovaya, Sennaya, 4)
NevskiyGDvor = Span(Nevskiy, GDvor, 4)
PNevskogo1PNevskogo2 = Span(PNevskogo1, PNevskogo2, 3)
TInstitut1TInstitut2 = Span(TInstitut1, TInstitut2, 2)
VosstaniyaMayakovskaya = Span(Vosstaniya, Mayakovskaya, 3)
VladimirskayaDostoevskaya = Span(Vladimirskaya, Dostoevskaya, 3)
PushkinskayaZvenigorodkaya = Span(Pushkinskaya, Zvenigorodskaya, 3)
SportivnayaSportivnaya2 = Span(Sportivnaya, Sportivnaya2, 4)

N = len(Station.registry)
routes = [[300] * N for _ in range(N)]

for i in range(N):
    for j in range(i):
        if i != j:
            for span in Span.registry:
                if set(span.stations) == {Station.registry[i], Station.registry[j]}:
                    routes[i][j] = routes[j][i] = span.time
        else:
            routes[i][j] = 0
