class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def __str__(self):
        matrix = f"{list(self.rows)}".replace("[[", "[")
        matrix = f"{matrix}".replace("]]", "]")
        matrix = f"{matrix}".replace("], [", "]\n[")
        return f"{matrix}".replace(", ", " ")

    def __add__(self, other):
        try:
            my_list = []
            for el in list(self.rows):
                sum_list = []
                for i in el:
                    sum_m = i + \
                        list(other.rows)[
                            list(self.rows).index(el)][el.index(i)]
                    sum_list.append(sum_m)
                my_list.append(sum_list.copy())
                sum_list.clear()
            return Matrix(my_list)
        except IndexError:
            return "Введенные данные некорректны"


a = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(f'First matrix:\n{a}')
print(f'Second matrix:\n{b}')
print(f'Sum of matrices:\n{a + b}')