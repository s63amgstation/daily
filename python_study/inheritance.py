class Country:
    """super class"""

    name = ''
    population = ''
    capital =''

    def show_super(self):
        print('국가 클래스의 메소드')
    

class Korea(Country):
    """sub class"""

    def __init__(self,name):
        self.name = name
    
    def show(self):
        super().show_super()
        print("국가명 : ",self.name)