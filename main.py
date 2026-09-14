def second_largest(numbers: list[float]) -> float:
    """מחזיר את המספר השני-בגודלו ברשימה. מניח לפחות 2 ערכים שונים."""
    unique_sorted = sorted(set(numbers), reverse=True)
    if len(unique_sorted) < 2:
        raise ValueError("נדרשים לפחות 2 ערכים שונים")
    return unique_sorted[1]


print(second_largest([3, 1, 4, 1, 5, 9, 2]))  # 5
class Rectangle:
    """מייצג מלבן לפי רוחב וגובה."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        """מחזיר את שטח המלבן."""
        return self.width * self.height


rect = Rectangle(4, 5)
print(rect.area())  # 20
