"""
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение,
а целенаправленное.
7.	Формируется матрица F следующим образом: скопировать в нее А и если в С количество нулевых элементов в нечетных столбцах,
чем количество нулевых  элементов в четных столбцах, то поменять местами С и В симметрично,
иначе С и Е поменять местами несимметрично. При этом матрица А не меняется.
После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение:
A*AT – K * FТ, иначе вычисляется выражение (AТ +G-F-1)*K, где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""
import time
import random
import numpy as np

print("\nРезультат работы программы:")
try :
    rows = int(input("Введите количество строк (столбцов) квадратной матрицы больше 3 : "))
    while rows < 4 :
        rows = int(input("Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы больше 3 :"))
    K = int(input("Введите число К="))
    start = time.time()
    A = np.zeros((rows,rows),dtype=int)
    F = np.zeros((rows,rows), dtype=int)

    for i in range (rows):     #формируем матрицу А
        for j in range(rows):
            A[i][j]=np.random.randint(-10,10)
            #A[i][j] = i*10+j
    middle = time.time()
    print("A time = ", middle - start,"\nmatrix A: \n",A)
    for i in range (rows):      #формируем матрицу F, копируя из матрицы А
        for j in range(rows):
            F[i][j]=A[i][j]

    count1=0
    count2=0
    for i in range(rows//2,rows):      #считаем кол-во нулей в четных и нечетных столбцах матрицы С
        for j in range(i + 1, rows, 1):
            if j % 2 == 1 and A[i][j] == 0:
                count1 += 1
            elif j % 2 == 0 and A[i][j] == 0:
                count2 += 1

    if count1>count2:    # в С кол-во нулевых элементов в нечетных столбцах больше,чем количество нулевых элементов
                         # в четных столбцах, то меняем местами С и В симметрично
        F[0:rows // 2, rows // 2 + rows % 2:rows] = A[rows // 2 + rows % 2:rows, rows // 2 + rows % 2:rows]
        F[rows // 2 + rows % 2:rows, rows // 2 + rows % 2:rows] = A[0:rows // 2, rows // 2 + rows % 2:rows]
    else:  #С и Е меняем местами несимметрично
        F[0:rows // 2, 0:rows // 2] = A[rows // 2 + rows % 2:rows, rows // 2 + rows % 2:rows]
        F[rows // 2 + rows % 2:rows, rows // 2 + rows % 2:rows] = A[0:rows // 2, 0:rows // 2]

    middle2 = time.time()
    print("\n matrix F: \n", F)

    if np.linalg.det(A) == 0 or np.linalg.det(F) == 0:
        print("\nМатрица A или F вырождена => нельзя вычислить")
    elif np.linalg.det(A) > sum(F.diagonal()):
        A = np.dot(np.dot(A, np.transpose(A)), K * np.transpose(F))  # 1 формула
        finish = time.time()
        print("\nопределитель матрицы А больше суммы диагональных элементов матрицы F","\nA time = :", finish - middle2,"\n",A)
    else:
        A = (np.transpose(A) + np.tril(A) - np.linalg.inv(F)-1) # 2 формула
        finish = time.time()
        print("\nопределитель матрицы А меньше суммы диагональных элементов матрицы F", "\nТреугольная матрица из А :\n",np.tril(A) ,"\nA time = :", finish - middle2, "\n",A,"\n")

    for i in A:  # делаем перебор всех строк матрицы
        for j in i:  # перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()

except ValueError:
    print("\nЭто не число")
except FileNotFoundError:
    print(
        "\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
    print("\nВремя работы программы:  ")