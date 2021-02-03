class CustomClass:

    def add_instance_method(self, a, b):
        return a+b

    @classmethod
    def add_class_method(cls,a,b):
        return a+b

    @staticmethod
    def add_static_method(a,b):
        return a+b