import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 25, 4) == 100

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 27, 3) == 9

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 18, 3) == 15

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 24, 26) == 50