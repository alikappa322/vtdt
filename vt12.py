import random
a = [random.randrange(50) for i in range(20)]
print("массив через рандом: ",a)
a1 = [5,4,3,1,2,1, 22, 31,48, 2, 1,99, 42, 22, 67, 82, 15, 61, 67]
b1 = [1, 4, 2, 6, 3, 22, 66, 33, 82, 11, 2, 3, 4, 5]
def func(X):
    a_max = 0
    i_max = 0
    k = 0.5
    for i in range(len(X)):
        if X[i]>a_max:
            a_max = X[i]
            i_max = i
    for n in range(len(X)):
        if n > i_max:
            X[n] = k
    print(X)
print("massiv a1")
func(a1)
print("b1")
func(b1)
print("huinia")
func(a)