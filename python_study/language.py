class Language:
    default_language = 'English'

    def __init__(self):
        self.show = '나의 언어는 '+self.default_language

    @classmethod
    def class_my_language(cls):
        return cls()

    @staticmethod
    def static_my_language():
        return Language()

    def print_language(self):
        print(self.show)


class Korean(Language):
    default_language = 'Korean'

"""
>>> from language import *
>>> a = KoreanLanguage.static_my_language()
>>> b = KoreanLanguage.class_my_language()
>>> a.print_language()
나의 언어는English
>>> b.print_language()
나의 언어는한국어
"""