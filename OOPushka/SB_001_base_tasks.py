# 9
class Figure:
    type_fig = 'ellipse'
    color = 'red'

fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'
del fig1.color
# print(' '.join([key for key in fig1.__dict__.keys()]))

# 10
class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'

p1 = Person()
print(hasattr(p1.__dict__,'job'))