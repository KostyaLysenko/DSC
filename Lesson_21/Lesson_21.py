# # A = [[1,2,3,4],
# #      [-5,12,7,21],
# #      [-6,30,5,23]]
# # print(A)
# # print(A[0])
# # print(A[0][3])
# # print(A[1][-1])
# #
X= [[2,4],
    [6,5]]
Y=[[3,5],
   [4,6]]
Z= [[0,0],
   [0,0]]

for i in range(len(X)):
    for l in range(len(X[0])):
        Z[i][l] = X[i][l]-Y[i][l]

for r in Z:
    print(r)
# # #Множення матриць


# length = len(X)
# result_matrix = [[0 for i in range(length)] for i in range(length)]
# for i in range(length):
#   for j in range(length):
#     for k in range(length):
#        result_matrix[i][j] += X[i][k] * Y[k][j]
# print(result_matrix)

# #
# # # Транспонування матриці
# #
# # XXX= [[5,12],
# #       [45,17],
# #       [56,23]]
# # ZZZ=[[0,0,0],
# #      [0,0,0]]
# # for i in range(len(XXX)):
# #     for l in range(len(XXX[0])):
# #         ZZZ[l][i]= XXX[i][l]
# # for r in ZZZ:
# #     print(r)
# #
# #
import numpy as np
# a = np.array([[1,2,3],[3,4,5]])
# print(a)
# print(type(a))
# b=np.array([[1,2,3],[3,4,5]], dtype=complex)
# print(b)
#
# z_matrix=np.zeros((2,4))
# print(z_matrix)
#
# print(np.shape(a))
# A= np.arange(12).reshape(2,6)
# print(A)
#
# AAA=A.reshape(1, 12)
# print(AAA)
#
# print(A[0][-1])
#
a = np.array([[2,4],
    [6,5]])
b = np.array([[3,5],
   [4,6]])
#
# C= a+b
# print(C)
c=a@b
print(c)
#
# S=np.array([[1,1],[2,1],[3,-3]])
# print(S.transpose())
# a=[[1,2,1],
#    [3,4,1]]
#
# b = [[1,2],
#      [1,2],
#      [1,2]]
# print(len(a))
# print(len(a[0]))
# print(len(b))
# print(len(b[0]))
#
# # приведение нулевой матрицы к виду максимальных значений
#
# if len(a)>len(b):
#     if len(a[0]) > len(b[0]):
#         print(np.zeros((len(a),len(a[0]))))
#     if len(a[0]) < len(b[0]):
#         print(np.zeros((len(a), len(b[0]))))
# if len(a)<len(b):
#     if len(a[0]) < len(b[0]):
#         print(np.zeros((len(b),len(b[0]))))
#     if len(a[0]) > len(b[0]):
#         print(np.zeros((len(b), len(a[0]))))
#
#
# # a=([[2,4,5],
# #     [6,5,6],
# #     [9,3,1]],
# #
# #     [[3,5,9],
# #    [4,6,7],
# #    [5,7,2]])
# #
# #
# # matrix1=a[0]
# # matrix2=a[1]
# # print(matrix2)
#
#
#
a=[[2,4,5],
    [6,5,6],
    [9,3,1]]

a[1][0]=a[0][0]*(-4)+a[1][0]
a[1][1]=a[0][1]*(-4)+a[1][1]
a[1][2]=a[0][2]*(-4)+a[1][2]
print(a)
