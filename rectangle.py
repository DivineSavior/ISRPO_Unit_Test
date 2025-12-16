def area(a, b):
    """Вычисляет площадь прямоугольника"""
    if a <= 0 or b <= 0:
        raise ValueError("Стороны должны быть положительными")
    return a * b

def perimeter(a, b):
    """Вычисляет периметр прямоугольника"""
    if a <= 0 or b <= 0:
        raise ValueError("Стороны должны быть положительными")
    return 2 * (a + b)