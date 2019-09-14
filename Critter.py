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

    def __pas_time(self):
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
        self.__pas_time()

    def eat(self, food = 4):
        print("<3")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pas_time()

    def paly(self, fun = 4):
        print(":)")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pas_time()

def main():
    print("Создание зверюшек.")
    crit1 = Critter("Зверюшка1")
    crit2 = Critter("Зверюшка2")

    Critter.status()

    crit1.talk()
    crit1.eat()
    crit1.play()

    print(crit1.mood)

main()

