class Par:
    def __init__(self, pr):
        self.r = pr


    def GetS(self):
        return (4 * 3.14 * (self.r**2))

    def GetV(self):
        return ((4/3) * 3.14 * self.r)

    def GetD(self):
        return self.r / 2

    def Info(self):
        print('-' * 20)
        print('Шар: \n')
        print('Радиус шара: ', (self.r))
        print('Объем: ', self.GetV())
        print('Диаметр: ', self.GetD())
        print('Площадь: ', self.GetS())
        print('-' * 20)

    def Load(path_to_file):
        d = open(path_to_file).read().strip().split()
        tmp = Par(float(d[0]))
        return tmp

p1 = Par(20)
p1.Info()

