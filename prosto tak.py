    # 0 1 2 3 4 5   6  7   8  9 10 11  12  13  14  15  16  17  18
a1 = [5,4,3,1,2,1, 22, 31,48, 2, 1,99, 42, 22, 67, 82, 15, 61, 67]
b1 = [1, 4, 2, 6, 3, 22, 66, 33, 82, 11, 2, 3, 4, 5]
def func(X):
    a_max = 0
    i_max = 0
    k = 0.5
    for i in range(len(a1)):
        if a1[i]>a_max:
            a_max = a1[i]
            i_max = i
    for n in range(len(a1)):
        if n > i_max:
            a1[n] = 0.5
    print(X)
func(a1)
func(b1)
