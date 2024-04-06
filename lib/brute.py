def pack_shapes(shapes, width=8, height=11):
    # Создаем пустую матрицу для распределения фигур
    grid = [['.' for _ in range(width)] for _ in range(height)]

    def can_place_shape(shape, x, y, rotation):
        # Проверяем, помещается ли фигура в указанные координаты с учетом поворота
        for point in shape:
            rotated_point = rotate_point(point, rotation)
            new_x = x + rotated_point[0]
            new_y = y + rotated_point[1]
            if not (0 <= new_x < width and 0 <= new_y < height):
                return False
            if grid[new_y][new_x] != '.':
                return False
        return True

    def place_shape(shape, x, y, rotation, label):
        # Распределяем фигуру в матрице с учетом поворота
        for point in shape:
            rotated_point = rotate_point(point, rotation)
            new_x = x + rotated_point[0]
            new_y = y + rotated_point[1]
            grid[new_y][new_x] = label

    def rotate_point(point, rotation):
        # Поворачиваем точку вокруг начала координат на указанный угол
        x, y = point
        if rotation == 90:
            return [-y, x]
        elif rotation == 180:
            return [-x, -y]
        elif rotation == 270:
            return [y, -x]
        else:
            return [x, y]  # Без поворота

    # Перебираем фигуры и распределяем их в багажнике
    label = 1
    for shape in shapes:
        placed = False
        for rotation in [0, 90, 180, 270]:  # Проверяем все возможные повороты
            for y in range(height):
                for x in range(width):
                    if can_place_shape(shape, x, y, rotation):
                        place_shape(shape, x, y, rotation, str(label))
                        label += 1
                        placed = True
                        break
                if placed:
                    break
            if placed:
                break

    return grid

# Пример использования функции
shapes = [
    # Фигура размером 4x4
    [[0, 0], [1, 0], [2, 0], [3, 0], [0, 1], [1, 1], [2, 1], [3, 1], [0, 2], [1, 2], [2, 2], [3, 2], [0, 3], [1, 3], [2, 3], [3, 3]],
    # Фигура размером 3x3
    [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]],
    # Фигура размером 2x2
    [[0, 0], [1, 0], [0, 1], [1, 1]],
    # Фигура размером 2x3
    [[0, 0], [1, 0], [0, 1], [1, 1], [0, 2], [1, 2]],
    # Фигура размером 1x4
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    # Фигура размером 4x1
    [[0, 0], [1, 0], [2, 0], [3, 0]],
]
result = pack_shapes(shapes)
for row in result:
    print(' '.join(row))
