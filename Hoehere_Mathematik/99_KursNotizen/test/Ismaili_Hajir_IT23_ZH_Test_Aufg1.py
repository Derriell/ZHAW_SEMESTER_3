import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]])

B = np.array([[5, 4, 3, 2], [4, 3, 2, 5], [3, 2, 5, 4], [2, 5, 4, 3]])

b = np.array([1, 2, 3, 4])


# a

Ab = np.dot(A, b)
Bb = np.dot(B, b)
AT = A.T
BT = B.T
ATA = np.dot(AT, A)
BTB = np.dot(BT, B)

print("A = ", A)
print("B = ", B)
print("b = ", b)
print("Ab: \n", Ab)
print("Bb: \n", Bb)
print("AT: \n", AT)
print("BT: \n", BT)
print("ATA: \n", ATA)
print("BTB: \n", BTB)

# b

result_b = np.dot(A[3, :], B[:, 1])
print("A[3,] mal B[,1]:\n", result_b)

# c

sum_column_A = np.sum(A, axis=0)
sum_row_sum_column_A = np.sum(sum_column_A)

sum_row_B = np.sum(B, axis=1)
sum_column_sum_row_B = np.sum(sum_row_B)

print("Summe der Spalten von A: ", sum_column_A)
print("Summe der Summen der Spalten von A: ", sum_row_sum_column_A)

print("Summe der Zeilen von B: ", sum_row_B)
print("Summe der Summen der Zeilen von B: ", sum_column_sum_row_B)


