import os

def list_files(startpath):
    structure = []  # Список для хранения структуры проекта

    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        structure.append('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            structure.append('{}{}'.format(subindent, f))
    
    return structure

if __name__ == '__main__':
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Получение абсолютного пути к текущему скрипту
    #project_directory = os.path.join(current_directory, 'serving_ml')  # Присоединение 'serving_ml' к текущему пути
    structure = list_files(current_directory)

    # Сохранение структуры в файл struc.txt
    with open('struc.txt', 'w') as file:
        for item in structure:
            file.write("%s\n" % item)