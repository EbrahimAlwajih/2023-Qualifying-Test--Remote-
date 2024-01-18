
A = [0] * (142)

A[1], A[2], A[3] = 1, 2, 3

for i in range (4, 142):
    temp = (A[i - 3] + A[i - 2] * A[i - 1]) 
    A[i] = temp % 113

print (A[141])