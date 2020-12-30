import os
import csv

class CarBase:
    """Включает атрибуты: car_type, photo_file_name, brand, carrying."""
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        """Получение расширения файла изображения с помощью os.path.splitext"""
        extension = os.path.splitext(self.photo_file_name)
        if extension[1] in ('.jpg', '.jpeg', '.png', '.gif'):
            return extension[1]
        # else:
        #     print("extension is wrong")
        # return extension[1]



class Car(CarBase):
    """Дополнительно включает количество пассажиров"""
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    """Дополнительно включает размеры кузова"""
    def __init__(self, brand, photo_file_name, carrying, body_whl=''):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        try:
            if body_whl != '' and body_whl.count('x') == 2:
                body_whl_str = body_whl.rsplit(sep='x')
                self.body_length = float(body_whl_str[0])
                self.body_width = float(body_whl_str[1])
                self.body_height = float(body_whl_str[2])
            # print(body_length, body_width, body_height)
            else:
                self.body_length = self.body_width = self.body_height = 0.0
        except ValueError:
            self.body_length = self.body_width = self.body_height = 0.0


    def get_body_volume(self):
        """Возвращает объем кузова"""
        self.value = self.body_length * self.body_width * self.body_height
        return self.value


class SpecMachine(CarBase):
    """Дополнительно включает атрибут Дополнительно"""
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def get_car_list(csv_filename):
    """Прочитать файл построчно при помощи модуля CSV, функция возвращает список объектов"""
    with open(csv_filename, encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        # next(reader)  # пропускаем заголовок
        car_list = []
        for row in reader:
            row_car_list = list(reader)

        for i in range(len(row_car_list)):
            if row_car_list[i][0] != '' and row_car_list[i][1] != '' and row_car_list[i][3] != '' and row_car_list[i][5] != '':
                ext = os.path.splitext(row_car_list[i][3])
                if ext[1] in ('.jpg', '.jpeg', '.png', '.gif'):
                    if row_car_list[i][0] == 'car' and row_car_list[i][2] != '' and row_car_list[i][4] == '' and \
                            row_car_list[i][6] == '':
                        car_object = Car(row_car_list[i][1], row_car_list[i][3], row_car_list[i][5], row_car_list[i][2])
                        car_list.append(car_object)

                    if row_car_list[i][0] == 'truck' and row_car_list[i][2] == '' and row_car_list[i][6] == '':
                        if row_car_list[i][4] == '':
                            # row_car_list[i][4] = '0.0x0.0x0.0'
                            car_object = Truck(row_car_list[i][1], row_car_list[i][3], row_car_list[i][5], row_car_list[i][4])
                            car_list.append(car_object)
                        else:
                            car_object = Truck(row_car_list[i][1], row_car_list[i][3], row_car_list[i][5], row_car_list[i][4])
                            car_list.append(car_object)
                    if row_car_list[i][0] == 'spec_machine' and row_car_list[i][2] == '' and row_car_list[i][4] == '' \
                            and row_car_list[i][6] != '':
                        car_object = SpecMachine(row_car_list[i][1], row_car_list[i][3], row_car_list[i][5], row_car_list[i][6])
                        car_list.append(car_object)
    return car_list
# ===========================================
# import csv
# import os.path
#
#
# class CarBase():
#     """базовый класс для транспортных средств"""
#
#     # атрибут для хранения обязательных параметров класса, описывающего транспортное средство
#     required = []
#
#     def __init__(self, brand, photo_file_name, carrying):
#         self.brand = self.validate_input(brand)
#         self.photo_file_name = self.validate_photo_filename(photo_file_name)
#         self.carrying = float(self.validate_input(carrying))
#
#     def validate_input(self, value):
#         """метод валидации данных, возвращает значение, если оно валидно,
#         иначе выбрасывает исключение ValueError"""
#         if value == '':
#             raise ValueError
#         return value
#
#     def validate_photo_filename(self, filename):
#         for ext in ('.jpg', '.jpeg', '.png', '.gif'):
#             if filename.endswith(ext) and len(filename) > len(ext):
#                 return filename
#         raise ValueError
#
#     def get_photo_file_ext(self):
#         _, ext = os.path.splitext(self.photo_file_name)
#         return ext
#
#     @classmethod
#     def create_from_dict(cls, data):
#         """создает экземпляр класса из словаря с параметрами"""
#         parameters = [data[parameter] for parameter in cls.required]
#         return cls(*parameters)
#
#
# class Car(CarBase):
#     """класс описывающий автомобили для перевозок людей"""
#     car_type = "car"
#     required = ['brand', 'photo_file_name', 'carrying', 'passenger_seats_count']
#
#     def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
#         super().__init__(brand, photo_file_name, carrying)
#         self.passenger_seats_count = int(self.validate_input(passenger_seats_count))
#
#
# class Truck(CarBase):
#     """класс описывающий автомобили для перевозок грузов"""
#     car_type = "truck"
#     required = ['brand', 'photo_file_name', 'carrying', 'body_whl']
#
#     def __init__(self, brand, photo_file_name, carrying, body_whl):
#         super().__init__(brand, photo_file_name, carrying)
#         self.body_length, self.body_width, self.body_height = self.parse_whl(body_whl)
#
#     def get_body_volume(self):
#         """возвращает объем кузова"""
#         return self.body_length * self.body_width * self.body_height
#
#     def parse_whl(self, body_whl):
#         """возвращает реальные размеры кузова length, width, height"""
#         try:
#             length, width, height = (float(c) for c in body_whl.split("x", 2))
#         except Exception:
#             length, width, height = 0.0, 0.0, 0.0
#         return length, width, height
#
#
# class SpecMachine(CarBase):
#     """класс описывающий спецтехнику"""
#
#     car_type = "spec_machine"
#     required = ['brand', 'photo_file_name', 'carrying', 'extra']
#
#     def __init__(self, brand, photo_file_name, carrying, extra):
#         super().__init__(brand, photo_file_name, carrying)
#         self.extra = self.validate_input(extra)
#
#
# def get_car_list(csv_filename):
#     """возвращает список объектов, сохраненных в файле csv_filename"""
#
#     car_types = {'car': Car, 'spec_machine': SpecMachine, 'truck': Truck}
#     csv.register_dialect('cars', delimiter=';')
#     car_list = []
#
#     with open(csv_filename, 'r') as file:
#         reader = csv.DictReader(file, dialect='cars')
#         for row in reader:
#             try:
#                 car_class = car_types[row['car_type']]
#                 car_list.append(car_class.create_from_dict(row))
#             except Exception:
#                 pass
#
#     return car_list
#
#
# if __name__ == '__main__':
#     pass
