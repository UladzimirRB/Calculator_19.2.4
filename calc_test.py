import pytest
from app.calculator import Calculator

class TestCalculator:

    def setup(self):
        self.a = Calculator()

    def test_adding_succedfull(self):
        # self.calc = Calculator
        assert self.a.adding(1, 1) == 2

    def test_multiply(self):
        # self.calc = Calculator
        assert self.a.multiply(2, 3) == 6

    def test_adding_unsuccedfull(self):
        # self.calc = Calculator
        assert self.a.adding(1, 1) == 3

    def test_subtraction(self):
        assert self.a.subtraction(8, 2) == 6

    def test_division(self):
        assert self.a.division(8, 2) == 4

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.a.division(1, 0)

    def teardown(self):
        print(" Выполнение метода Teardown \n")
