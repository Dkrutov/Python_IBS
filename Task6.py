
class Animal:
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
instas_Animal_3=Animal_3()
instas_Animal_4=Animal_4()

print(instas_Animal_2.voice())
print(instas_Animal_3.voice())
print(instas_Animal_4.voice())










