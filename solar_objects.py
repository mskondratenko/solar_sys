# coding: utf-8
# license: GPLv3

def color_guess(color_input):
    '''
    Function transforms name of the color to RGB form
    
    Keyword arguments:
    color_input -- name of the color to transform
    '''
    input_filename = 'colors.txt'
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            color_name, color_number = line.split(':')
            if (color_name == color_input):
                color_number = color_number.split(',')
                for i in range(3):
                    color_number[i] = int(color_number[i])
                return color_number

class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    def __init__(self, line):
        self.type, self.R, self.color, self.m, self.x, \
        self.y, self.Vx, self.Vy = line.split()
        self.R = int(self.R)
        self.color = color_guess(self.color)
        self.m = float(self.m)
        self.x = float(self.x)
        self.y = float(self.y)
        self.Vx = float(self.Vx)
        self.Vy = float(self.Vy)


        self.Fx = 0
        """Сила по оси **x**"""

        self.Fy = 0
        """Сила по оси **y**"""


class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    def __init__(self, line):
        self.type, self.R, self.color, self.m, self.x, \
        self.y, self.Vx, self.Vy = line.split()
        self.R = int(self.R)
        self.color = color_guess(self.color)
        self.m = float(self.m)
        self.x = float(self.x)
        self.y = float(self.y)
        self.Vx = float(self.Vx)
        self.Vy = float(self.Vy)

        self.Fx = 0
        """Сила по оси **x**"""

        self.Fy = 0
        """Сила по оси **y**"""
