# Библиотека вычисления площадей фигур

## Возможности

- Вычисление площади круга по радиусу
- Вычисление площади треугольника по трём сторонам
- Проверка, является ли треугольник прямоугольным
- Фабричная функция для создания фигур по имени
- Лёгкое расширение для других фигур
- Полиморфизм: работа с разными фигурами через единый интерфейс

## Установка

1. Скопируйте папку `shape_lib` в свой проект.
2. (Опционально) Установите через pip из архива:
   ```
   pip install git+https://github.com/Mililitr/shape_lib.git
   ```

## Использование

```python
from area import Circle, Triangle, create_shape

c = Circle(2)
print(c.area())  # 12.566370614359172

t = Triangle(3, 4, 5)
print(t.area())      # 6.0
print(t.is_right())  # True

# Фабричная функция
shape = create_shape("circle", 3)
print(shape.area())  # 28.274333882308138

# Полиморфизм
shapes = [Circle(1), Triangle(5, 12, 13)]
for s in shapes:
    print(s.area())
```

## Тесты

Запустите тесты командой:
```
python -m unittest discover tests
```

## Контакты для поддержки

- Email: support@yourcompany.com
- Телефон: +7 (999) 123-45-67