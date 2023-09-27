# 4
# class MediaPlayer:
#     def open(self, file):
#         self.filename = file
#     def play(self):
#         print('Воспроизведение',self.filename)
#
# media1 = MediaPlayer()
# media2 = MediaPlayer()
# media1.open('filemedia1')
# media2.open('filemedia2')
# media1.play()
# media2.play()

# 5
# class Graph:
#     LIMIT_Y = [0, 10]
#
#     def set_data(self, data):
#         self.data = data
#
#     def draw(self):
#         l = ' '.join([str(y) for y in self.data if self.LIMIT_Y[0] <= y <= self.LIMIT_Y[1]])
#         print(l)
#
# graph1 = Graph()
# graph1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph1.draw()

# 6
# import sys
#
#
# class StreamData:
#     def create(self, fields, lst_values):
#         if len(fields) == len(lst_values):
#             try:
#                 for i in range(len(fields)):
#                     setattr(self, fields[i], lst_values[i])
#                 return True
#             except:
#                 return False
#         else:
#             False
#
#
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
#
#
# sr = StreamReader()
# data, result = sr.readlines()
# print(data)
# print(result)

# 9
# import sys
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     def insert(self, data):
#         for item in data:
#             self.lst_data.append(dict(zip(self.FIELDS,item.split())))
#
#     def select(self, a, b):
#         return self.lst_data[a:b+1]
#
# db = DataBase()
# db.insert(lst_in)
# print(db.select(1,2))

# 10
class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        self.tr.pop(eng, False)

    def translate(self, eng):
        # if eng in list(self.tr.keys()):
        return self.tr[eng]
            # print(' '.join(list(self.tr[eng])))

tr = Translator()

tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')

# tr.translate('tree')[0]
# print('перевод car до удаления:', tr.translate('car'))
tr.remove('car')
# print('перевод car после удаления:', tr.translate('car'))
print(*tr.translate('go'))