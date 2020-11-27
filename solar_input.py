# coding: utf-8
# license: GPLv3

from color_guess import color_guess_num
from solar_objects import Star, Planet
from solar_vis import DrawableObject

def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем

            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star(line)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet(line)
                objects.append(planet)
            else:
                print("Unknown space object")

    return [DrawableObject(obj) for obj in objects]


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.

    Строки должны иметь следующий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла

    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            obj_out = obj.obj
            print('test')
            print(str(obj_out.m))
            out_file.write(
                  obj_out.type + " " + str(obj_out.R) + " " + color_guess_num(obj_out.color) +
                      " " + str(obj_out.m) + " " + str(obj_out.x) + " " + str(obj_out.y) +
                      " " + str(obj_out.Vx) + " " + str(obj_out.Vy) + '\n')
            # FIXME!


if __name__ == "__main__":
    print("This module is not for direct call!")
