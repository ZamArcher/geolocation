class FileReader:
    """Конструктор этого класса принимает только 1 параметр - путь до файла на диске"""

    def __init__(self, filename='example.txt'):
        self.filename = filename

    def read(self):
        """Возвращает строку - содержимое файла, путь к которому был указан при создании экземпляра класса"""
        try:
            file = open(self.filename)
            return file.read()
        except IOError:
            return ""


def main():
    x = FileReader('example.txt')
    print(x.read())


if __name__ == "__main__":
    main()
