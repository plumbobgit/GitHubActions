import calculator


class TestCalculator:

    def test_add(self):
        assert calculator.add(2, 2) == 4

    def test_subtract(self):
        assert calculator.subtract(2, 2) == 0

    def test_multiply(self):
        assert calculator.multiply(2, 2) == 4

    def test_divide(self):
        assert calculator.divide(2, 2) == 1
