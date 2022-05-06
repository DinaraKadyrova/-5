# Вариант 7

С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное. Вид матрицы А:  E  B
                                                                                                                                        C  D
Формируется матрица F следующим образом: скопировать в нее А и если в С количество нулевых элементов в нечетных столбцах, чем количество нулевых 
элементов в четных столбцах, то поменять местами С и В симметрично, иначе С и Е поменять местами несимметрично. При этом матрица А не меняется. 
После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A*AT – K * FТ, иначе вычисляется 
выражение (AТ +G-F-1)*K, где G-нижняя треугольная матрица, полученная из А. Выводятся по мере формирования А, F и все матричные операции 
последовательно.
