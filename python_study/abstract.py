from abc import *


class AbstractCountry(metaclass=ABCMeta):
    name = '국가명'
    population = '인구'
    capital = '수도'

    def show(self):
        print('국가 클래스의 메소드입니다.')

    @abstractclassmethod
    def show_captital(self):
        print("수도는?")

class Korea(AbstractCountry):

    def __init__(self, name,population, capital):
        self.name = name
        self.population = population
        self.capital = capital

    def show_name(self):
        print('국가 이름은 : ', self.name)

    def show_captital(self):
        super().show_captital()
        print("hello?")