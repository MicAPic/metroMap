from time import sleep


class Station:
    registry = []

    def __init__(self, name, line):
        self.registry.append(self)
        self.name = name
        self.line = line
        self.id = len(self.registry) - 1

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


PVeteranov = Station('Проспект Ветеранов', 'красн')
LeninskyP = Station('Ленинский проспект', 'красн')
Avtovo = Station('Автово', 'красн')
KirovskyZ = Station('Кировский завод', 'красн')
Narvskaya = Station('Нарвская', 'красн')
Baltiyskaya = Station('Балтийская', 'красн')
TInstitut1 = Station('Технологический институт-1', 'красн')
Pushkinskaya = Station('Пушкинская', 'красн')
Vladimirskaya = Station('Владимирская', 'красн')
Vosstaniya = Station('Площадь Восстания', 'красн')
Chernyshevskaya = Station('Чернышевская', 'красн')
PLenina = Station('Площадь Ленина', 'красн')
Vyborgskaya = Station('Выборгская', 'красн')
Lesnaya = Station('Лесная', 'красн')
PMuzhestva = Station('Площадь Мужества', 'красн')
Politeh = Station('Политехническая', 'красн')
Akademicheskaya = Station('Академическая', 'красн')
GrazdanskiyP = Station('Гражданский проспект', 'красн')
Murino = Station('Девяткино', 'красн')

Kupchino = Station('Купчино', 'син')
Zvezdnaya = Station('Звездная', 'син')
Moskovskaya = Station('Московская', 'син')
ParkP = Station('Парк Победы', 'син')
Elektrosila = Station('Электросила', 'син')
MVorota = Station('Московские ворота', 'син')
Frunzenskaya = Station('Фрунзенская', 'син')
TInstitut2 = Station('Технологический институт-2', 'син')
Sennaya = Station('Сенная площадь', 'син')
Nevskiy = Station('Невский проспект', 'син')
Gorkovskaya = Station('Горьковская', 'син')
PSkaya = Station('Петроградская', 'син')
ChRechka = Station('Чёрная речка', 'син')
Pionerskaya = Station('Пионерская', 'син')
Udelnaya = Station('Удельная', 'син')
Ozerki = Station('Озерки', 'син')
PProsvet = Station('Проспект Просвещения', 'син')
Parnas = Station('Парнас', 'син')

Rybatskoe = Station('Рыбацкое', 'зелен')
Obuhovo = Station('Обухово', 'зелен')
Proletarskaya = Station('Пролетарская', 'зелен')
Lomonosovskaya = Station('Ломоносовская', 'зелен')
Elizarovskaya = Station('Елизаровская', 'зелен')
PNevskogo1 = Station('Площадь Александра Невского-1', 'зелен')
Mayakovskaya = Station('Маяковская', 'зелен')
GDvor = Station('Гостиный двор', 'зелен')
VOskaya = Station('Василеостровская', 'зелен')
Primorskaya = Station('Приморская', 'зелен')
Novokrestovskaya = Station('Зенит', 'зелен')
Begovaya = Station('Беговая', 'зелен')

Spasskaya = Station('Спасская', 'желт')
Dostoevskaya = Station('Достоевская', 'желт')
LigovskyP = Station('Лиговский проспект', 'желт')
PNevskogo2 = Station('Площадь Александра Невского-2', 'желт')
Novocherkasskaya = Station('Новочеркасская', 'желт')
Ladozhskaya = Station('Ладожская', 'желт')
PBolshevikov = Station('Проспект Большевиков', 'желт')
Dybenko = Station('Улица Дыбенко', 'желт')

Shushary = Station('Шушары', 'фиолетов')
Dunaiskaya = Station('Дунайская', 'фиолетов')
PSlavy = Station('Проспект Славы', 'фиолетов')
Mezhdunarodnaya = Station('Муждународная', 'фиолетов')
Buharestskaya = Station('Бухарестская', 'фиолетов')
Volkovskaya = Station('Волковская', 'фиолетов')
OKanal = Station('Обводный канал', 'фиолетов')
Zvenigorodskaya = Station('Звенигородская', 'фиолетов')
Sadovaya = Station('Садовая', 'фиолетов')
Admiralteiskaya = Station('Адмиралтейская', 'фиолетов')
Sportivnaya = Station('Спортивная', 'фиолетов')
Chkalovskaya = Station('Чкаловская', 'фиолетов')
KrestovskyO = Station('Крестовский остров', 'фиолетов')
StarayaD = Station('Старая Деревня', 'фиолетов')
KomendantskiyP = Station('Комендантский проспект', 'фиолетов')

for station in Station.registry:
    print(station)
    # sleep(0.25)

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
KrestovskyOStarayaD = Span(Chkalovskaya, StarayaD, 3)
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
# for span in Span.registry:
#     print(span)

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
# print(routes)
