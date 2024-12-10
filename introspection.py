import inspect


def introspection_info(obj):
    info = {}

    # Тип объекта
    info['type'] = type(obj).__name__

    # Атрибуты объекта
    info['attributes'] = [attr for attr in dir(obj) if not attr.startswith('__')]
    # Методы объекта
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    # Модуль, к которому объект принадлежит
    info['module'] = obj.__module__

    # Другие интересные свойства объекта
    if hasattr(obj, '__dict__'):
        info['dict'] = obj.__dict__
    if hasattr(obj, '__class__'):
        info['class'] = obj.__class__.__name__
    if hasattr(obj, '__bases__'):
        info['bases'] = [base.__name__ for base in obj.__bases__]

    return info


# Создаем свой класс и объект для лучшего понимания
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, z):
        return self.x + self.y + z


obj = MyClass(2, 3)

# Вызываем функцию introspection_info
obj_info = introspection_info(obj)
print(obj_info)
