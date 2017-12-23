import random
a1 = [random.randrange(50) for i in range(20)]
print(a1)

b1 = [random.randrange(50) for i in range(20)]
print(b1)
k = int(input("chislo: "))
des = 10
def func(mas,k_d):
    i_max = 0
    mas_max = 0
    for i in range(len(mas)):
        if mas[i]>=mas_max:
            mas_max = mas[i]
            i_max = i
    if k_d not in mas:
        mas[i_max] = k_d
        print(mas)
    else:
        print("число {} уже есть".format(k_d))
func(a1,k)
func(b1,des)
