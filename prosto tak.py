a1 = [1,22,31,2,1,42,22,1000,67,82,15,61,67]

b1 = [1,4,2,6,3,22,66,33,82,11,2,3,4,5,123415]
k = int(input("chislo: "))
des = 10
def func(mas,k_d):
    i_max = 0
    mas_max = 0
    for i in range(len(mas)):
        if mas[i]>mas_max:
            mas_max = mas[i]
            i_max = i
    if k_d not in mas:
        mas[i_max] = k_d
        print(mas)
    else:
        print("число {} уже есть".format(k_d))
func(a1,k)
func(b1,des)
