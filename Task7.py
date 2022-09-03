
class Animal:
    num_of_insts=0
    def __init__(self):
        Animal.num_of_insts = Animal.num_of_insts + 1
    def print_num():
        print('Создано ', Animal.num_of_insts, ' экземпляра')
    print_num=staticmethod(print_num)
    def voice(self):
        pass

class Animal_2(Animal):
    def voice(self):
        return "Вывод Animal_2"

class Animal_3(Animal):
    def voice(self):
        return "Вывод Animal_3"

class Animal_4(Animal):
    def voice(self):
        return "Вывод Animal_4"

instas_Animal_2=Animal_2()
print(instas_Animal_2.voice())
instas_Animal_3=Animal_3()
print(instas_Animal_3.voice())
instas_Animal_4=Animal_4()
print(instas_Animal_4.voice())
Animal.print_num()













