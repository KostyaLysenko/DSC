#Завдання 1
class Automobile:
    def __init__(self, mark, colour, volume):
        self.mark= mark
        self.colour = colour
        self.volume = volume

    def move_forward(self):
        return "Їхатиму вперед"
    def move_back(self):
        return "Їхатиму назад"
class AdAutomobile(Automobile):
    def move_left(self):
        return "Їхатиму наліво"
    def move_right(self):
        return "Їхатиму направо"

opel = Automobile("Opel", "Сірий", 2)
volvo = AdAutomobile("Volvo", "Синій", 3)

print(opel.colour)
print(opel.move_forward())
print(opel.move_back())
print(volvo.move_left())
#############
# Завдання 2


import string
class TextProcessor:
    def __init__(self, my_line):
        self.my_line = my_line
        self.line_punkt = ''
    def get_clean_string(self):
       for i in self.my_line:
            if i in string.punctuation:
                self.line_punkt = self.line_punkt + i
                self.my_line = self.my_line.replace(i,'')
       return self.my_line
    def __is_punktiantian(self):
        if len(self.line_punkt) != 0:
            return True
        else:
            return False
class TextLoader(TextProcessor):
    def __init__(self, text_processor):
        self.__text_processor = TextProcessor(text_processor)
        self.__clean_string= ""
    @property
    def set_clean_string(self):
        self.__clean_string = self.__text_processor.get_clean_string()
        print(f"Виводиться вже очищений текст: {self.__clean_string}")
class DataInterface(TextLoader):
    #в цій частині не розібравсь до кінця які саме рядки треба порахувати
    def __init__(self, text_processor2):
        self.__text_processor2 = TextLoader(text_processor2)
    def process_texts(self):
        for i in self.__text_processor2:
            self.count_lines= sum(i)
        print(self.count_lines)
        # print(self.__text_processor2(sum("\n")))

text = TextProcessor(input())
print(text.get_clean_string())
text._TextProcessor__is_punktiantian()

text2 = TextLoader(input())
text2.set_clean_string
# text.is_punktiantian()
text3 = DataInterface("")
text3.process_texts
############################
Завдання 3
from math import *
class Parallelogram:
    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght
    def get_area(self):
        n=2
        return self.lenght * (sqrt((self.width ** n) - (self.lenght ** n)))
class Sqare(Parallelogram):
    def __init__(self, width):
        self.width=width
    def get_area(self):
        n = 2
        return self.width**n

parallelogram = Parallelogram(25, 15)
sqare = Sqare(25)

print(parallelogram.get_area())
print(sqare.get_area())

