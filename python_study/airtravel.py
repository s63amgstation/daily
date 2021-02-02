class Flight:
    __class_attr = []

    def __init__(self):
        self.__class_attr = []

    def add_instance_attr(self, number):
        self.__class_attr.append(number)
        print('instance_attr: '+self.__class_attr)    

    @classmethod
    def add_class_attr(cls, number):
        cls.__class_attr.append(number)
    @classmethod
    def print_attr(cls):
        print(cls.__class_attr)     

    # def add_class_attr(self, number):
    #     Flight.class_attr.append(number)        


    ## 출처 : https://wikidocs.net/16072