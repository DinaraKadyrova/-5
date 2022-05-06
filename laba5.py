'''
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение,
а целенаправленное.
7.	Формируется матрица F следующим образом: скопировать в нее А и если в С количество нулевых элементов в нечетных столбцах,
чем количество нулевых  элементов в четных столбцах, то поменять местами С и В симметрично,
иначе С и Е поменять местами несимметрично. При этом матрица А не меняется.
После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение:
A*AT – K * FТ, иначе вычисляется выражение (AТ +G-F-1)*K, где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно.
'''
import random
import time
import numpy as np

print("\nРезультат работы программы:\n \nЛокальное время", time.ctime())
try:
    rows = int(input("\nВведите количество строк квадратной матрицы >3:"))
    while rows<4:
        rows = int(input("\nВведите количество строк квадратной матрицы >3:"))
    K = int(input("\nВведите число K="))
    start = time.time()
    A = np.zeros((rows,rows),dtype=int)  #задаём матрицы A и F = 0
    F = np.zeros((rows,rows),dtype=int)

    t0 = time.time()
    print("инициализация матриц", t0-start)

    for i in range(rows):  # заполняем матрицу А
        for j in range(rows):
            A[i][j] = random.randint(-10,10)
            #A[i][j] = i*10+j
            '''
            if i < j and j < rows - 1 - i:
                A[i][j] = 1
            elif i < j and j > rows - 1 - i:
                A[i][j] = 2
            elif i > j and j > rows - 1 - i:
                A[i][j] = 3
            elif i > j and j < rows - 1 - i:
                A[i][j] = 4
            '''
    t1 = time.time()
    print("\nA time = ", t1-t0)
    print(A)
    for i in range(rows):   # заполняем матрицу F
        for j in range(rows):
            F[i][j] = A[i][j]

    count1=0
    count2=0
    for i in range(rows//2,rows):
        for j in range(i + 1, rows, 1):
            if j % 2 == 1 and A[i][j] == 0:
                count1 += 1
            elif j % 2 == 0 and A[i][j] == 0:
                count2 += 1

    if count1>count2:
        F[0:rows // 2, rows // 2 + rows % 2:rows] = A[rows // 2 + rows % 2:rows, rows // 2 + rows % 2:rows]
        F[rows // 2 + rows % 2:rows, rows // 2 + rows % 2:rows] = A[0:rows // 2, rows // 2 + rows % 2:rows]
    else:
        F[0:rows // 2, 0:rows // 2] = A[rows // 2 + rows % 2:rows, rows // 2 + rows % 2:rows]
        F[rows // 2 + rows % 2:rows, rows // 2 + rows % 2:rows] = A[0:rows // 2, 0:rows // 2]

    print("\nF time = ", 0)
    print(F)
    for i in range(rows): #корректируем А
        A[i][i] = 0
        if np.linalg.det(A) == 0 or np.linalg.det(F) == 0:
            print("\nМатрица A или F вырождена\nвычисления невозможны")
        elif np.linalg.det(A) > sum(F.diagonal()):
            A = np.dot(np.dot(A, np.transpose(A)), K * np.transpose(F)) # 1 формула
            finish = time.time()
            print("определитель матрицы А больше суммы диагональных элементов матрицы F")
        else:
            print("\nmatrix A   ")
            #print(np.tril(A))
            A = (np.transpose(A) + np.tril(A) - np.linalg.inv(F)-1) # 2 формула
            print("определитель матрицы А меньше суммы диагональных элементов матрицы F",
                  "\nТреугольная матрица из А :\n", np.tril(A))

        for i in A:  # делаем перебор всех строк матрицы
            for j in i:  # перебираем все элементы в строке
                print("%5d" % j, end=' ')
            print()

        finish = time.time()
        result = finish - start
        print("Program time: " + str(result) + "seconds.")

except ValueError:
    print("\n это не число")
except FileNotFoundError:
    print(
        "\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
    print("\nВремя работы программы:  ", time.process_time(), "seconds")