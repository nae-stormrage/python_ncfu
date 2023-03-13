class Par:
    def __init__(self, px1, py1, pz1, px2, py2, pz2):
        self.x1 = px1
        self.y1 = py1
        self.z1 = pz1
        self.x2 = px2
        self.y2 = py2
        self.z2 = pz2


    def GetDlina(self):
        return abs(((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2 + (self.z2 - self.z1)**2)**(1/2))

    def GetR1(self):
        return abs(((self.x1 - 0) ** 2 + (self.y1 - 0) ** 2 + (self.z1 - 0) ** 2) ** (1 / 2))

    def GetR2(self):
        return abs(((self.x2 - 0) ** 2 + (self.y2 - 0) ** 2 + (self.z2 - 0) ** 2) ** (1 / 2))

    def Info(self):
        print('-' * 20)
        print('Отрезок в пространстве:')
        print('Координаты в пространстве: ', self.x1, self.y1, self.z1, self.x2, self.y2, self.z2)
        print('Длина отрезка: ', self.GetDlina())
        print('Расстояние от начало координат до начала и конца координат отрезка соответственно: ', self.GetR1(),' и ', self.GetR2())
        print('-' * 20)

    def Load(path_to_file):
        d = open(path_to_file).read().strip().split()
        tmp = Par(float(d[0]),float(d[0]),float(d[0]),float(d[0]),float(d[0]),float(d[0]))
        return tmp

p1 = Par(1, 1, 1, 2, 2, 2)
p1.Info()

