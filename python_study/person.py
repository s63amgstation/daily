class Person:
    def __init__(self, *args):
        self.hello = '안녕하세요.'
        self.name1 = args[0]
        self.age = args[1]
        self.address = args[2]
 
    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name1))
 
maria = Person('마리아', 20, '서울시 서초구 반포동','장근영')
maria.greeting()    # 안녕하세요. 저는 마리아입니다.
 
print('이름:', maria.name1)       # 마리아
print('나이:', maria.age)        # 20
print('주소:', maria.address)    # 서울시 서초구 반포동