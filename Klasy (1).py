from random import randint

class Character():
    def __init__(self):
        self.name = ''
        self.health = 1
        self.staff = ''
        self.atak1 = 1
        self.atak2 = 1
        self.heal_power = 1

    def do_damage(self, enemy):
        x = randint(0, 10)
        if x < 7:
            enemy.health = enemy.health - self.atak1
            print("Phi, taki atak to o kant...ziemi...rozbić. Zabrales wrogowi", self.atak1, "zycia. Leszczu.")
        elif x == 7:
            print("Nie trafiles. Kretyn.")
        else:
            enemy.health = enemy.health - self.atak2
            print("Nadal nie wierze, ze przezyjesz. Zabrales wrogowi ", self.atak2,
                  "zycia, ale jeszcze się nie ciesz, będzie tylko gorzej")

    def heal(self):
        self.health = self.health + self.heal_power

class Nikt_Ciekawy(Character):
    def __init__(self):
        Character.__init__(self)
        self.health = 20
        self.atak1 = 6
        self.atak2 = 10
        self.staff = []
        self.heal_power = 4
    def add_staff(self, staff):
        self.staff.append(staff)

class Ogr(Character):
    def __init__(self):
        Character.__init__(self)
        input("Pff, tylko leszcze przekładają życie nad atak i intelekt. #teamelfy. Pewnie się jeszcze nazwiesz Hulk.")
        self.name = "Hulk"
        self.health = 40
        self.atak1 = 2
        self.atak2 = 5
        self.staff = []
        self.heal_power = 10
    def add_staff(self, staff):
        self.staff.append(staff)

class Elf(Character):
    def __init__(self):
        Character.__init__(self)
        self.health = 10
        self.atak1 = 18
        self.atak2 = 25
        self.staff = []
        self.heal_power = 2
    def add_staff(self, staff):
        self.staff.append(staff)

class Enemy():
    def __init__(self):
        self.name = ''
        self.health = 1
        self.atak1 = 1
        self.atak2 = 1

    def do_damage_enemy(self, character):
        x = randint(0, 10)
        if x >= 0 and x < 7:
            character.health = character.health - self.atak1
            print("Teraz wiesz, czemu nie masz szans? Zabrał Ci", self.atak1, "życia. Leszczu.")
        elif x == 7:
            print("Nie trafił. Kretyn.")
        else:
            character.health = character.health - self.atak2
            print("O skurczybyk! Zabrał ci", self.atak2, "życia. Nie wyżyjesz, nie ma szans.")

class Doglin(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.name = 'Doglina.'
        self.health = 10
        self.atak1 = 3
        self.atak2 = 5

class Wrog_zbrodniczego_Rezimu(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.name = 'Zaczepiste Monstrum.'
        self.health = 25
        self.atak1 = 5
        self.atak2 = 10

class Wielki_Szczur(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.name = 'Wielgachnego,spasionego szczura.'
        self.health = 4
        self.atak1 = 2
        self.atak2 = 5

class Straz_Krolowej_Kucy(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.name = 'Straż królowej Kucy, która drzemała w skrzyni.'
        self.health = 10
        self.atak1 = 3
        self.atak2 = 5

class Siostry_Godlewskie(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.name = 'Najpaskudniejsze i najbardziej okrutne monstra jakie ma w swojej kolekcji Krolowa Kucy: Siosty Godlewskie.'
        self.health = 99999999
        self.atak1 = 1000000
        self.atak2 = 6666666666666

class Walka(Character, Enemy):
    def walka(self, character, enemy):
        Character.__init__(self)
        Enemy.__init__(self)
        while character.health > 0 and enemy.health > 0:
            print("1. Atak. \n2. Regeneracja")
            x = (input())
            if x == '1':
                Character.do_damage(character, enemy)
                if enemy.health < 1:
                    break
            elif x == '2':
                Character.heal(character)
                print("Uleczono o", character.heal_power)
            else:
                print("No brawo, znowu nie umiesz w cyferki...")
            Enemy.do_damage_enemy(enemy, character)
            print("Zycie gracza", character.health)
            print("Zycie przeciwnika", enemy.health)
        if character.health < 1:
            print("Ups")
            return 15
        else:
            print("Przeciwnik nie zyje")
            print("Zycie gracza", character.health)
            print("Zycie przeciwnika", enemy.health)