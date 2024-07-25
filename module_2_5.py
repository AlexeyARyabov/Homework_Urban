def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)

x = int(input('введите количество строк:'))
y = int(input('введите количество столбцов:'))
z = int(input('введите значение элементов матрицы:'))

get_matrix(x, y, z)