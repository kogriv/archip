# input = [3, 5, 2, 7, 5, 3, 8, 3]
# output = [3, 5]

def func(inp):
    outp = []
    for i in inp:
        print("before",inp)
        inp.remove(i)
        print("after",inp)
        if i in inp and i not in outp:
            outp.append(int(i))
    
    return outp

def find_duplicates(arr):
    # Создаем словарь для подсчета элементов
    counts = {}
    
    # Подсчитываем количество вхождений каждого элемента
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    # Отбираем элементы, которые встречаются более одного раза
    result = [num for num, count in counts.items() if count > 1]
    
    return result

def func(inp):
    outp = []
    seen = set()  # Множество для отслеживания уже встреченных элементов

    for i in inp:
        if i in seen and i not in outp:
            outp.append(i)
        seen.add(i)
    
    return outp


print("Введите числа:")
inp = input().split()
inp = [int(i) for i in inp]
#print(inp)


print(func(inp))
