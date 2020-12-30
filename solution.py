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

