class SimpleCalculator:

    def _check_types(self, a: int, b: int) -> None:
        """Vérifie que a et b sont des int."""
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Les paramètres doivent être des entiers.")

    def fsum(self, a: int, b: int) -> int:
        """Additionne deux entiers."""
        self._check_types(a, b)
        return a + b

    def substract(self, a: int, b: int) -> int:
        """Soustrait deux entiers."""
        self._check_types(a, b)
        return a - b

    def multiply(self, a: int, b: int) -> int:
        """Multiplie deux entiers."""
        self._check_types(a, b)
        return a * b

    def divide(self, a: int, b: int) -> float:
        """Divise deux entiers. Retourne un float."""
        self._check_types(a, b)
        if b == 0:
            raise ZeroDivisionError("Division by zero.")
        return float(a / b)
