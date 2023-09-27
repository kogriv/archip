from pprint import  pprint
class Point:
    color = 'red'
    circle_radius = 3
    # pprint(locals(), width=60, compact=True)

# Поместить все атрибуты и методы класса Point в globals()
# for name, value in Point.__dict__.items():
#     if not name.startswith("__"):  # Исключаем "магические" методы
#         globals()[name] = value


# pprint(globals(), width=60, compact=True)

class Car:
    pass

setattr(Car, 'model', "Тойота")
setattr(Car, 'color', "Розовый")
setattr(Car, 'number', "П111УУ77")
pprint(Car.__dict__['color'])