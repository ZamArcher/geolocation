"""В этом задании вам нужно создать интерфейс для работы с файлами. Интерфейс должен предоставлять следующие возможности
по работе с файлами:
- чтение из файла, метод read возвращает строку с текущим содержанием файла
- запись в файл, метод write принимает в качестве аргумента строку с новым содержанием файла
- сложение объектов типа File, результатом сложения является объект класса File, при этом создается новый файл
  и файловый объект, в котором содержимое второго файла добавляется к содержимому первого файла. Новый файл должен
  создаваться в директории, полученной с помощью функции tempfile.gettempdir. Для получения нового пути можно
  использовать os.path.join.
- возвращать в качестве строкового представления объекта класса File полный путь до файла
- поддерживать протокол итерации, причем итерация проходит по строкам файла
При создании экземпляра класса File в конструктор передается полный путь до файла на файловой системе.
Если файла с таким путем не существует, он должен быть создан при инициализации."""

import tempfile
import sys
import uuid
from os.path import exists, join


class File(object):

    def __init__(self, filename=None):
        self.filename = filename
        self.tmp_path = tempfile.gettempdir()

        if not exists(self.filename):
            open(self.filename, 'w').close()

    def __add__(self, obj):
        new_path = join(
            self.tmp_path,
            str(uuid.uuid4().hex)
        )
        new_file = type(self)(new_path)
        new_file.write(self.read() + obj.read())

        return new_file

    def __iter__(self):
        with open(self.filename) as f:
            return iter(f.readlines())

    def __next__(self):
        return self

    def __str__(self):
        return self.filename

    def write(self, text):
        with open(self.filename, 'w') as f:
            f.write(text)
            print(len(text))
        # return self

    def read(self):
        with open(self.filename, 'r') as f:
            return f.read()


if __name__ == '__main__':
    file = File(sys.argv[1])
    print('Iteration:')
    for line in file:
        print(line)
    print('__str__ test:')
    print(file)
    print('write() test:')
    file.write('a b\n1 2\n3 4')
    for line in file:
        print(line)
    print('__add__ test:')

    a = File(sys.argv[1])
    b = File(sys.argv[1])
    c = a + b
    print(c)
    for line in c:
        print(line)
