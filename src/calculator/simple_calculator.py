class SimpleCalculator:

    def _check_types(self, a: int, b: int) -> None:
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Les arguments doivent être des entiers.")

    def fsum(self, a: int, b: int) -> int:
        self._check_types(a, b)
        return a + b

    def substract(self, a: int, b: int) -> int:
        self._check_types(a, b)
        return a - b

    def multiply(self, a: int, b: int) -> int:
        self._check_types(a, b)
        return a * b

    def divide(self, a: int, b: int) -> float:
        self._check_types(a, b)
        if b == 0:
            raise ZeroDivisionError("La division par zéro n'est pas autorisée.")
        return float(a / b)