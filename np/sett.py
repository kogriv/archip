import numpy as np
# Numpy - это библиотека для работы с многомерными
# массивами и матрицами. Некоторые основные настройки numpy:
n=3
np.set_printoptions(precision=n) #- определяет количество знаков после запятой при выводе массивов numpy.

np.set_printoptions(suppress=True) #- отключает вывод научной нотации при выводе массивов numpy.

np.seterr(all='ignore') #- игнорирует все ошибки при выполнении операций с массивами numpy.

# Правильная настройка параметров библиотек
# numpy может значительно повысить эффективность
# работы с ней. Однако, не стоит забывать,
# что некоторые параметры могут влиять на
# результаты выполнения операций, поэтому
# следует использовать их с осторожностью и
# только тогда, когда это действительно необходимо.