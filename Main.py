from random import randint
import Klasy

nr = 1
def pokoj2():
    enemy = Klasy.Wielki_Szczur()
    print("Pomieszczenie, do ktorego wszegles jest ciemne i wigotne. Dostrzegasz jednak, ze cos porusza sie w kacie pokoju. \n 1. Sprawdz co to \n 2. Zignoruj to i idz do nastepnego pomieszczenia.")
    x = input()
    if x == '1':
        print("UWAGA!!!!!!!")
    elif x == '2':
        print("Cos jednak zastepuje ci droge.")
    else:
        print("ehhhhh....")
        return 15
    print("Napotykasz", enemy.name, "Wyczuwam kłopoty")
    print("Jego zycie to", enemy.health)
    walka = Klasy.Walka()
    pa = walka.walka(gracz, enemy)
    if pa!=15:
        return 3
    else:
        return 15

def wybor_drogi_03():
    print("Przechodzac dalej dostrzegasz, ze korytarz rozwidla sie.")
    print("Ktora droge wybierzesz?\n 1. Idz w lewo.\n 2. Idz prosto.")
    x = input()
    if x == '1':
        return 4
    elif x == '2':
        return 10
    else:
        print("Kretyn...")
        return 15

def pokoj4():
    enemy = Klasy.Wrog_zbrodniczego_Rezimu()
    print("Droge zastepuje ci", enemy.name, " Bron sie!")
    print("Jego zycie to", enemy.health)
    walka = Klasy.Walka()
    pa = walka.walka(gracz, enemy)
    if pa!=15:
        return 5
    else:
        return 15

def uczta():
    print("Widzisz przed soba ogromny stol zastawiony jedzeniem.")
    print("Nagle przejscie za toba zamyka sie, a pokoj wypelniaja biesiadnicy.")
    print("1. Walcz z nimi")
    print("2. Dolacz do zabawy")
    a = input()
    if a == '1':
        print("Powalaja cie i przywiazuja do krzesla, a nastepnie wlewaja dziwny napoj do gardla. Pszzzeessttajerz wieedzeici cccoooo ssje dz...")
        return randint(2,5)
    elif a == '2':
        print("Zasiadasz do stolu i wtedy pojawia sie On. FOOD EMPEROR. Juz wiesz, ze nie bedzie latwo. Biesiadnicy zaczynaja polewac.")
        print("1. Pij z nimi")
        print("2. Odmow")
        b = input()
        if b == '1':
            print("Wszyscy krzycza: Chlusniem, bo usniem! Po kilku kolejkach wiesz, ze przegiales...")
            return randint(6,10)
        elif b == '2':
            print("Slyszysz: Kto nie pije, ten nie zyje!")
            return 15
        else:
            print("Ty tak serio nie umiesz w te cyferki?")
            return 15
    else:
        print("Ciekawy ruch")
        return 6


def wybor_drogi_06():
    print("Przechodzac dalej dostrzegasz, ze korytarz rozwidla sie.")
    print("Ktora droge wybierzesz?\n 1. Idz w lewo.\n 2. Idz prosto.")
    x = input()
    if x == '1':
        return 7
    elif x == '2':
        return 8
    else:
        print("Kretyn...")
        return 15

def pokoj7():
    print('Z mrokow wynurza sie ogromna krypta, wsparta kolumnami z wilgotnego, oblazlego glonem i mchem drewna. Sciany strasza zebami krat, a przez cisze przedziera sie smetne skomlenie. Podchodzisz blizej, a wtedy glony na kolumnach rozblyskaja delikantnym, fluorescencyjnym światlem i ruszaja ku Tobie, na szczescie bardzo powoli. Jak wszystko w Krainie Kucy - sa zajebiscie glodne.\n')
    print('Chcesz je tyknac?')
    print("1. Nie")
    print("2. Domysl sie")
    tknij = input()
    if tknij == '1':
        print('Coz za przezornosc!')
    elif tknij == '2':
        gracz.health = gracz.health - 5
        if gracz.health <= 0:
            print("Glony pozeraja Cie w calosci. Jestes debilem")
            return 15
        else:
            print("Kretyn. Glony wsysaja Twoja dlon, przez co jest poparzona, fioletowa i sliska. No i tracisz 5 zdrowia, wiec wynosi ono", gracz.health, "\nGratuluje.")
    else:
        print("No prawie")
        return 15
    print("Z jednej z cel slychac zjadliwy smiech, a gdy niesmialo zblizasz sie do krat dostrzegasz, ze w kacie przycupnal kot i co chwila spluwa na pelznace ku niemu glony. Gdy Cie dostrzega, mruzy przebiegle slepka. Wlasnie otwiera pyszczek, by cos powiedziec gdy przerywa mu glosne CLANG, a w kraty sasiedniej celi uderza wielka kula futra.")
    podejdz = input('1. Podejdz do drugiej celi. \n2. Zostan przy kocie.  \n3. Uciekaj stamtad, nie jestes tu na pogaduszkach z futrzakami.')
    if podejdz == '3':
        return 6
    elif podejdz == '2':
        print("Kot: To tam, to sie nie przejmuj. To tylko Glupi Kundel, nikt wazny. Musisz mnie uwolnic, bo taki maricon jak ty nie wyjdzie stad zywy. Bardzo Cie kusilo dotknac te glony, hm? No wiec mnie potrzebujesz. Klucz gdzies sie poniewiera, poszukaj go.")
    elif podejdz == '1':
        print("Okazuje sie, ze kula futra to tak naprawde szpic wilczy - przeslodki, wlochaty i usmiechniety od ucha do ucha. \nPiesek: Ratunek! Tak sie ciesze, o boszu boszu! Idziemy na spacer, na wolnosc! Klucz! Klucz w skrzynce! ")
    print('Dostrzegasz skrzynie w kacie, ktora otwierasz. Okazuje sie, ze w jej wnetrzu odsypia uczte Straz Krolowej Kucy!')
    enemy = Klasy.Straz_Krolowej_Kucy()
    walka = Klasy.Walka()
    walka.walka(gracz, enemy)
    print("Zdobywasz klucze do obu cel")
    print("Kot: Uwolnij mnie! I NAWET SIE NIE WAZ UWALNIAC TEGO DEBILA! \nPiesek: Ratunek! Ratunek! O boszu boszu, pomoz!")
    towarzysz = input("Kogo chcesz uwolnic? \n1. Kota \n2. Psa \n3. Obojga")
    if towarzysz == 1:
        print("Otwierasz przed kotem drzwi, a on mruczy z zadowolenia. Pies zaczyna glosno szlochac. \nKot: Jednak nie jestes az tak głupi...*odwracajac sie do zalamanego psa* See ya later frajerejter! Chodzmy, towarzyszu!")
        gracz.add_staff('Towarzysz Kot')
        return 8
    elif towarzysz == 2:
        print("Gdy otwierasz drzwi przed pieskiem ten skacze na Ciebie z radosnym szczekaniem i przywala Cie toną futra. \nPiesek: Boszu boszu! Idziemy! Bedziemy super przyjaciolmi! Kocham Cie! \nKot: TY GLUPI KULASONIE! ZGINIESZ, ZDRAJCO! POPAMIETASZ MNIE!")
        gracz.add_staff('Towarzysz Pies')
        return 8
    elif towarzysz == 3:
        print("Gdy otwierasz obie cele kot rzuca sie z pazurami na psa. Futrzaki tocza sie po podlodze jako wielka kula lap, futra, pazurow i sliny. Nagle kot popycha psa w glony, ktore pochlaniaja nieszczesne stworzenie. Kot odwraca sie ku Tobie. \nKot: Ostrzegalem bys zabral tylko mnie... Chodzmy, towarzyszu.")
        gracz.add_staff('Towarzysz Kot')
        return 8
    else:
        return 15

def pokoj8():
    enemy = Klasy.Wrog_zbrodniczego_Rezimu()
    print("O nie! to kolejny", enemy.name, " chce cie powstrzymac przed dotarciem na bal!")
    print("Jego zycie to", enemy.health)
    walka = Klasy.Walka()
    pa = walka.walka(gracz, enemy)
    if pa!=15:
        return 9
    else:
        return 15

def szafa():
    print("Pomieszczenie, do ktorego wchodzisz, jest dobrze oswietlone, a po srodku majestatyczna Bumfight Spargl, nr 3 na liscie najlepszych kucy.")
    print("Witaj przyjacielu zbrodniczgo rezimu. Zgaduje, ze zmierzasz ma bal u krolowej.")
    print("Obowiazuje tam jednak dresscode, w ktory nie wpisuje sie twoj ubior")
    print("Musisz przebrac sie w cos z mojej szafy. Oto co w niej mam:")
    print("1. Lachmany")
    print("2. Dresy")
    print("3. Fancy stroj wieczorowy")
    print("4. Nie przebieraj sie")
    a = 0
    while a == 0:
        x = int(input())
        if x == 1:
            print("Ubierz cos innego, lachmany to moj styl.")
        elif x > 1 and x < 4:
            print("Podoba mi sie twoj styl. Przechodzisz dalej")
            return 11
        elif x == 4:
            print("ZNIEWAZYLES KROLOWA. KARA JEST SMIERC")
            return 15
        else:
            print("Czy naprawde tak trudno jest wybrac cyfre od 1 do 4?!")

def szyfr():
    print("Widzisz przed soba masywne drzwi z klodka.")
    print("1. Zawroc")
    print("2. Podejdz do klodki")
    a = input()
    if a == '1':
        return 3
    elif a == '2':
        print("Po dotknieciu klodki slyszysz glos w swojej glowie:")
        print("Aby przejsc dalej musisz rozwiazac starozytna zagadke starozytnych doglinow. Masz przed soba 3-cyfrowy szyfr. Pierwsza cyfra okresla ilosc serduszek jakie ma dzdzownica, mimo tego, ze nie ma nikogo do kochania. Druga i trzecia musisz odgadnac na podstawie podanej sumy wszystkich trzech cyfr. Pamietaj, ze druga jest wieksza lub rowna od trzeciej.")
        print("Masz 3 proby. Jesli zawiedziesz, idziesz pentelke.")
        szanse = 0
        z = 5
        y = randint(0, 9)
        x = randint(0, 9)
        if x > y:
            y, x = x, y
        else:
            pass
        suma = z + y + x
        print("Suma:", suma)
        while szanse < 3:
            szanse += 1
            a = int(input("Wpisz pierwsza cyfre"))
            b = int(input("Wpisz druga cyfre"))
            c = int(input("Wpisz trzecia cyfre"))
            if a != z or b != y or c != x:
                print("Tracisz szanse.")
                if szanse == 3:
                    print("Nie jestes na tyle sprytny, zeby podac ten szyfr. Musisz zawrocic.")
                    return 3
            else:
                print("Hmmmm... Nie sadzilam, ze jestes az tak sprytny.")
                print("Drzwi otwieraja sie.")
                return 11
    else:
        print("Debil.")
        return 3

def medrzec():
    zg = 0
    zm = 0
    print("Medrzec: Witaj, Aby przejsc dalej musisz pokonać mię w starożytnej grze, ktora zwie sie kamien, papier, nozyce.")
    while zm < 3 and zg < 3:
        m = randint(1, 3)
        print("1 - nozyce")
        print("2 - papier")
        print("3 - kamien")
        print("wybierz mondrze")
        g = int(input())
        if m == g:
            print("Mamy impas. Sprobujmy ponownie")
        elif m == 1 and g == 2:
            print("HA! Wiedzialem, ze tak zrobisz!")
            zm += 1
            print("//Zwycięstwa gracza =", zg)
            print("//Zwycięstwa medrca =", zm)
        elif m == 1 and g == 3:
            print("Miales zwyczajnie szczescie...")
            zg += 1
            print("//Zwycięstwa gracza =", zg)
            print("//Zwycięstwa medrca =", zm)
        elif m == 2 and g == 1:
            print("Miales zwyczajnie szczescie...")
            zg += 1
            print("//Zwycięstwa gracza =", zg)
            print("//Zwycięstwa medrca =", zm)
        elif m == 2 and g == 3:
            print("HA! Wiedzialem, ze tak zrobisz!")
            zm += 1
            print("//Zwycięstwa gracza =", zg)
            print("//Zwycięstwa medrca =", zm)
        elif m == 3 and g == 1:
            print("HA! Wiedzialem, ze tak zrobisz!")
            zm += 1
            print("//Zwycięstwa gracza =", zg)
            print("//Zwycięstwa medrca =", zm)
        elif m == 3 and g == 2:
            print("Miales zwyczajnie szczescie...")
            zg += 1
            print("//Zwycięstwa gracza =", zg)
            print("//Zwycięstwa medrca =", zm)
        else:
            print("TY DZBANIE, miało być od 1 do 3, czy ty nie umiesz czytac?!")
            print("za kare tracisz jedna szanse")
            zm += 1

        if zg == 3:
            print("gratuluje zwycięstwa. Mozesz przejść dalej")
            return 12
        elif zm == 3:
            print("no to idż zmondrzyj!")
            return 4

def pokoj12():
    enemy = Klasy.Siostry_Godlewskie()
    print("Tego sie nie spodziewales. Przejscia pilnuja", enemy.name, "Probujesz uciec, ale drzwi sie za toba zamknely.\n")
    print("Ich zycie to", enemy.health)
    walka = Klasy.Walka()
    pa = walka.walka(gracz, enemy)
    if pa==15:
        print("Upadasz na ziemie, siostry zaczynaja spiewac Happy Birthday, twoje uszy krwawia, zaslaniasz je modlac sie o smierc.")
        print("Strazniczki sa upojone twoim cierpieniem. Przerywaja upiorna melodie i wybuchaja diabelskim smiechem, ktory przeszywa twoja dusze niczym tysiace sztyletow.")
        if gracz.staff[1] != '':
            print("Chwile nieuwagi siostr wykorzystuje twoj kompan.")
            if gracz.staff[1] == 'Towarzysz Pies':
                print("Skacze ku siostra i poteznymi szczekami przegryza im gardla")
            elif gracz.staff[1] == 'Towarzysz Kot':
                print("Skacze ku siostra i pazurami podrzyna im gardla")
            else:
                return 15
            print("Dziekujesz przyjacielowi i wspierajac sie na sobie nawzajem ruszecie ku nastepnemu pomiszczeniu")
            return 13
        else:
            print("Umierasz")
        return 15
    else:
        return 15

def pokoj13():
  if gracz.staff[1] == 'Towarzysz Pies':
    print('Wychodzicie ramie w lape na ogrony dziedziniec, oswietlony plonącym stosem, jednak imponujaca postura Twojego psiego towarzysza odstrasza podejrzanie zakapturzonych drani. Pies: Kto jest dobrym pieskiem i uratował Pana? HMMMM?')
    pogladz = int(input('Chcesz poglaskac pieska?\n 1. Jasne, ze tak, nie jestem kutafonem/bezdusznym sukinsynem \n 2.Jestem kutafonem'))
    if pogladz == 1:
      print('Piesek z zadowoleniem mruży oczyska i razem wchodzicie na salony Krolowej Kucy')
      return 14
    else:
      return 15

  else:
    print('Wychodzisz na ogromny dziedziniec oswietlony plonącym stosem i wtem czujesz na gardle ostre jak brzytew pazury. Kot: Ten bal jest za maly dla nas dwoch. Niech zyje zbrodniczy rezim!')
    odpowiedz = int(input('1. Odkrzyknij: Niech żyje zdbrodniczy rezim\n2. Zwyzywaj kota za zdrade'))
    if odpowiedz == 1:
      print('Kot patrzy na Ciebie z pogarda, ale tez lekkim usmiechem,giniesz bezbolesnie, jakbys zapadal w niekonczacy sie sen')
      return 15
    elif odpowiedz == 2:
      print('Kot *przewraca oczyma*: No po prostu debil... Giniesz powoli w okropnych meczarniach, a potem to, co zostaje z twych szczatkow plonie na stosie. Jestes potepiony! Yay!')
      return 15
    else:
      return 15

def zakonczenie():
    str = "  GRATULACJE  "
    print(str.center(80, '*'))
    print("Udało ci się dotrzec na bal krolowej \nBezwzgledna wladczyni dotrzymuje swojego slowa i spelnia twoje zyczenie. \nTwoja rodzina jest bezpieczna...\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n...przynajmniej narazie. ")

while nr != 15:
    print("Pokoj nr ", nr)
    if nr == 1:
        print("Zyjesz w swiecie kontrolowanym przez zbrodniczy rezim Krolowej Kucy. Rzadzi ona niepodzielnie twarda reka i nie toleruje slowa sprzeciwu.")
        print("Zycie przecietnego mieszkanca nie nalezy do najlatwiejszych, codzien musi liczyc sie z licznymi ograniczeniami oraz nieprzyjemnosciami takimi jak nieuzasadnione aresztowania.")
        print("Pech chcial, ze calkiem niedawno to wlasnie twoja rodzina zostala bezpodstawnie uwieziona w najbardziej rygorystycznej placowce jaka zna ten swiat.")
        print("Jest jednak szansa, zeby ich uratowac - bezwgledna tyranka organizuje bal.")
        print("Spelnia na nim zyczenia gosci.")
        print("Kazdy moze sprobowac sie tam dostac, jednak nie jest to latwe.")
        print("Po drodze napotkasz liczne niebezpieczenstwa i najprawdopodobniej czeka cie smierc w meczarniach...")
        print("Nie masz już jednak nic do stracenia, wiec decydujesz sie dotrzec na bal u krolowej...")
        a = input('Wybierz postac:\n1. Nikt Ciekawy \n2. Ogr \n3. Elf \n\nNumer mojej postaci to ')
        if a == '1':
            gracz = Klasy.Nikt_Ciekawy()
            gracz.name = input('Nazwij swoją nudną i przecietna postac...nie chce straszyc ale ogrem przynajmniej mialbys szansę...')
            print("Twoje parametry to")
            print("imie:", gracz.name)
            print("zycie:", gracz.health)
            print("atak:", gracz.atak1)
            print("zacny atak:", gracz.atak2)
        elif a == '2':
            gracz = Klasy.Ogr()
            print("Twoje parametry to")
            print("imie:", gracz.name)
            print("zycie:", gracz.health)
            print("atak:", gracz.atak1)
            print("zacny atak:", gracz.atak2)
        elif a == '3':
            gracz = Klasy.Elf()
            gracz.name = input('Z takim życiem daję Ci dwa pokoje, to najprawdopodobniej Twój największy błąd. Pasowałby Ci Nikt Ciekawy ;p. No dajesz, nazwij się jakoś oryginalnie')
            print("Twoje parametry to")
            print("imie:", gracz.name)
            print("zycie:", gracz.health)
            print("atak:", gracz.atak1)
            print("zacny atak:", gracz.atak2)
        else:
            print('Jestes idiota. Koniec gry')
            nr = 15
        czy = input("Czy chcesz wylosować tajemniczy przedmiot? \n1. Tak \n2. Nie ")
        if czy == '1':
            x = randint(1, 10)
            if x < 5:
                print("wylosowałeś noz! gratki, +4 do ataku")
                gracz.add_staff('noz')
                gracz.atak1 = gracz.atak1 + 4
                gracz.atak2 = gracz.atak2 + 4
                print("Twoje ataki to teraz\natak", gracz.atak1, "\nzacny atak", gracz.atak2, "\n a wyposazenie to",
                      gracz.staff)
                nr = 2
            elif x > 4 and x < 9:
                print("wylosowałes chelm, +4 do zycia. Nie ciesz sie, i tak zginiesz zanim dojdziesz do polowy gry")
                gracz.add_staff('chelm')
                gracz.health = gracz.health + 4
                print("Twoje zycie to teraz", gracz.health, "\na wyposazenie to", gracz.staff)
                nr = 2
            else:
                print("wylosowales 'Nagly zgon'. brawo. nie zyjesz")
                nr = 15
        elif czy == '2':
            print("Jestes tchorzem! Skoro nie chcesz nawet losowac, to nie możesz pojechać na bal. Giniesz deklu")
            nr = 15
        else:
            print("Nie umiesz odpowiadać na pytania. Wedle woli wszechwładnej Krolowej Kucy oznacza to smierc!")
            nr = 15
    elif nr == 2:
        nr = pokoj2()
    elif nr == 3:
        nr = wybor_drogi_03()
    elif nr == 4:
        nr = pokoj4()
    elif nr == 5:
        nr = uczta()
    elif nr == 6:
        nr = wybor_drogi_06()
    elif nr == 7:
        nr = pokoj7()
    elif nr == 8:
        nr = pokoj8()
    elif nr == 9:
        nr = szafa()
    elif nr == 10:
        nr = szyfr()
    elif nr == 11:
        nr = medrzec()
    elif nr == 12:
        nr = pokoj12()
    elif nr == 13:
        nr = pokoj13()
    elif nr == 14:
        zakonczenie()
    else:
        print("ciekawe")

