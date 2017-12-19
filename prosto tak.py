class Bolnica:
    def __init__(self, surname,name,otech,medcarta,diagnoz):
        self.surname = surname
        self.name = name
        self.otech = otech
        self.medcarta = medcarta
        self.diagnoz = diagnoz
def pacienty_diagnoz(bolnica_list,diagnoz):
    print("Пациенты имеющие данный диагноз: ")
    for bolnica in bolnica_list:
        if bolnica.diagnoz == diagnoz:
            print(bolnica.surname,bolnica.name,bolnica.otech)

def print_interval(pacienty, start, end):
    for pacient in pacienty:
        if start <= pacient.medcart < end:
            print(pacient.name)

def print_interval(pacient_list, start, end):
    for pacient in pacient_list:
        if start <= pacient.medcarta < end:
            print(pacient.name)

# class Clinic(Bolnica):
#     def __init__(self,maccive):
#         self.maccive = maccive
# def comps(self,clinic_list,pere):
#     for lul in clinic_list:
#         if lul.maccive == pere:
#             print(self.surname,self.name,self.otech, "работает в клинике {} ".format(lul.maccive))

arthas = Bolnica("Менетил","Артас","Нерзулович",100000,"Остеохондроз")
olzhas = Bolnica("Сапаров","Олжас","Нуркенович",200000,"Слабоумие")
vasya = Bolnica("Пупкин","Вася","Витальевич",300000,"Биполярность")
dasha = Bolnica("Петрова","Дарья","Николаевна",400000,"Бронхит")
aleksey = Bolnica("Ким","Алексей","Витальевич",500000,"Плохое зрение")
bolnye = [arthas,olzhas,vasya,dasha,aleksey]
pacienty_diagnoz(bolnye,input("Выберите любое из болезней: Остеохондроз, Слабоумие, Биполярность, Бронхит или же людей с плохим зрением: ",))
print("Интервал карты от 200к до 500к не включительно")
print_interval(bolnye, 200000, 500000)
massiv_clinic = ["Диамед","On Clinic","Ваше здоровье","Интертич","UroCenter"]
#comps(massiv_clinic,input("пишите Диамед, On Clinic, Ваше здоровье, Интертич, UroCenter: "))