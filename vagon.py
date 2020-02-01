class Vagon(object):
    def __init__(self, height, wide, long, maxMass, open, ready, x, y):
        self._maxMass = maxMass
        self._height = height
        self._wide = wide
        self._long = long
        self.__sizelimit = wide * long * height
        self._boxlist = []
        self._mass = 0
        self._size = 0
        self._notinBoxlist = []
        self.open = bool(open)
        self.ready = bool(ready)
        self._x = float(x)
        self._y = float(y)

    @property
    def wide(self):
        return self._wide

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def height(self):
        return self._height

    @property
    def long(self):
        return self._long

    @property
    def maxMass(self):
        return self._maxMass

    @property
    def boxlist(self):
        return self._boxlist

    @property
    def size(self):
        return self._size

    @property
    def notinBoxlist(self):
        return self._notinBoxlist

    @property
    def mass(self):
        return self._mass

    @property
    def sizelimit(self):
        return vagon.__sizelimit

    def checkMove(self):
        if self.ready is True:
            return True
        else:
            return False

    def checkInput(self, cargo):
        if cargo.w <= self.wide and cargo.h <= self.height and \
                cargo.l <= self.long and \
                cargo.m + self.mass <= self.maxMass and \
                self.sizelimit >= self._size + cargo.size and \
                self.open is True:
            return True
        else:
            return False

    def putInVagon(self, cargo):
        if self.checkInput(cargo) is True:
            self._size += cargo.size
            self._boxlist.append(cargo.name)
            self._mass += cargo.m
        else:
            self.notinBoxlist.append(cargo.name)

    def outputlast(self):
        lastCargo = self.boxlist.pop()
        return print('put out: ', lastCargo)

    def moveVagon(self, x, y):
        if self.checkMove() is True:
            self._x += x
            self._y += y

        else:
            return print('Vagon cant move')

    def __str__(self):
        return f"Max mass: {self.maxMass}\n" \
               f"Mass: {self.mass}\n" \
               f"Long: {self.long}\n" \
               f"Wide: {self.wide}\n" \
               f"Height: {self.height}\n" \
               f"Size: {self.size}\n" \
               f"Open: {self.open}\n" \
               f"Ready to move: {self.ready}\n" \
               f"Cargo list: {self.boxlist}\n" \
               f"Vagon x = {self.x}, y ={self.y}"


class Cargo(object):
    def __init__(self, name, height, wide, long, mass):
        self._m = mass
        self._l = long
        self._w = wide
        self._h = height
        self._size = long * height * wide
        self._name = name

    @property
    def w(self):
        return self._w

    @property
    def h(self):
        return self._h

    @property
    def l(self):
        return self._l

    @property
    def m(self):
        return self._m

    @property
    def size(self):
        return self._size

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"Name: {self._name}\n" \
               f"Mass: {self._m}\n" \
               f"Long: {self._l}\n" \
               f"Wide: {self._w}\n" \
               f"Height: {self._h}\n" \
               f"Size: {self._size}\n"


class Fridge(Cargo):
    pass


class Table(Cargo):
    pass


class Box(Cargo):
    pass


if __name__ == "__main__":
    vagon = Vagon(20, 40, 60, 20, True, False, 1, 1)
    fridge = Fridge('Fridge', 5, 5, 5, 5)
    table = Table('Table', 5, 5, 5, 5)
    box = Box('Box', 5, 5, 5, 5)
    box4 = Cargo('box4', 5, 5, 5, 5)
    box5 = Cargo('box5', 5, 5, 5, 5)
    box6 = Cargo('box6', 5, 5, 5, 5)
    box7 = Cargo('box7', 5, 5, 5, 5)
    box8 = Cargo('box8', 5, 5, 5, 5)
    box9 = Cargo('box9', 5, 5, 5, 5)
    box10 = Cargo('box10', 5, 5, 5, 5)
    vagon.putInVagon(fridge)
    vagon.putInVagon(table)
    vagon.putInVagon(box)
    print(box.__str__())
    print(vagon.boxlist)
    vagon.outputlast()
    print(vagon.boxlist)
    vagon.moveVagon(2, -5)
    print(vagon.__str__())
    print(table.__str__())
