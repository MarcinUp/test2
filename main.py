import unittest

class calculator():

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self):
        if isinstance(self._x, int) or isinstance(self._x, float):
            return self._x
        else:
            raise ValueError('Value type error, should be int or float but got %s' % type(self._x).__name__)

    @property
    def y(self):
        if isinstance(self._y, int) or isinstance(self._y, float):
            return self._y
        else:
            raise ValueError('Value type error, should be int or float but got %s' % type(self._y).__name__)


    def add(self):
        return self.x + self.y


class Test_calculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator(3, 7).add(), 11)


def main():
    return print(calculator(3, 7).add())

if __name__=="__main__":
    main()





