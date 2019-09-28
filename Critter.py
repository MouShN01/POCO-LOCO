#Моя зверюшка

class Critter(object):
    """Питомец"""
    total = 0

    @staticmethod
    def status():
        print("Общее число зверюшек", Critter.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total += 1

    def __str__(self):
        ans = "Имя - " + self.name + "\n"
        return ans

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверюшки не может быть пустым.")
        else:
            self.__name = new_name
            print("Имя зверюшки успешно изменено.")

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <=10:
            m = "не очень хорошо"
        elif 11 <= unhappiness <=15:
            print("не очень хорошо")
        else:
            m = "ужасно"
        return m
         

    def talk(self):
        print("Привет! Я - зверюшка. Меня зовут -", self.name, "я чувствую себя", self.mood)
        self.__pass_time()

    def eat(self, food = None):
        self.hunger -= int(input())
        print("<3")
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = None):
        self.boredom -= int(input())
        print(":)")
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("Как вы назовете свою зверюшку?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print \
        ("""
        Моя зверюшка

        0 - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        """)

        choice = input("Ваш выбор: ")
        print()

        if choice == "0":
            print("До свидания.")
        elif choice == "1":
            crit.talk()

        elif choice == "2":
            print("Сколько кг корма дать зверюшке?")
            crit.eat()

        elif choice == "3":
            print("Сколько вы хтите игратся с звеюшкой?")
            crit.play()

        else:
            print("Извините, в меню нет пункта", choice)

main()

