# coding: utf-8
# license: GPLv3


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    def __init__(self, line):
        self.type, self.R, self.color, self.m, self.x, \
        self.y, self.Vx, self.Vy = line.split()
        for el in (self.R, self.color, self.m, self.x,
                   self.y, self.Vx, self.Vy):
            el = int(el)

        self.Fx = 0
        """Сила по оси **x**"""

        self.Fy = 0
        """Сила по оси **y**"""


class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    def __init__(self):
        self.type, self.R, self.color, self.m, self.x, \
        self.y, self.Vx, self.Vy = line.split()
        for el in (self.R, self.color, self.m, self.x,
                   self.y, self.Vx, self.Vy):
            el = int(el)

        self.Fx = 0
        """Сила по оси **x**"""

        self.Fy = 0
        """Сила по оси **y**"""

